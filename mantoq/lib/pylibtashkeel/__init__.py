import importlib.resources as resources
from dataclasses import dataclass
from typing import Dict

import numpy as np
import onnxruntime

from . import assets
from .constants import ALL_VALID_DIACRITICS, DIACRITIC_CHARS
from .text_encoder import TextEncoder


@dataclass(frozen=True, slots=["original", "letters", "diacritics"])
class FeaturizedText:
    original: str
    letters: list[str]
    diacritics: list[str]

    @classmethod
    def extract_features(
        cls, text: str, correct_reversed: bool = True
    ) -> tuple[str, list[str], list[str]]:
        """
        Args:
        text (str): text to be diacritized
        Returns:
        text: the text as came
        text_list: all text that are not haraqat
        haraqat_list: all haraqat_list
        """
        if len(text.strip()) == 0:
            return text, [" "] * len(text), [""] * len(text)
        stack = []
        haraqat_list = []
        txt_list = []
        for char in text:
            # if chart is a diacritic, then extract the stack and empty it
            if char not in DIACRITIC_CHARS:
                stack_content = extract_stack(stack, correct_reversed=correct_reversed)
                haraqat_list.append(stack_content)
                txt_list.append(char)
                stack = []
            else:
                stack.append(char)
        if len(haraqat_list) > 0:
            del haraqat_list[0]
        haraqat_list.append(extract_stack(stack))
        return cls(text, txt_list, haraqat_list)


class LibtashkeelDiacritizer:

    def __init__(self) -> None:
        with resources.open_binary(assets, "libtashkeel.onnx") as f:
            model_bytes = f.read()
        self.session = onnxruntime.InferenceSession(
            model_bytes, providers=["CPUExecutionProvider"]
        )
        self.text_encoder = TextEncoder()
        self.input_pad_id = self.text_encoder.input_pad_id

    def __call__(self, input_sentences: list[str]) -> list[str]:
        input_sentences = [self.text_encoder.clean(sent) for sent in input_sentences]
        features = [FeaturizedText.extract_features(sent) for sent in input_sentences]
        char_inputs = [
            self.text_encoder.input_to_sequence("".join(feat.letters))
            for feat in features
        ]
        diac_hints = [
            self.text_encoder.target_to_sequence(feat.diacritics) for feat in features
        ]
        input_lengths = [len(i) for i in diac_hints]
        char_inputs = numpy_pad_sequences(char_inputs)
        diac_hints = numpy_pad_sequences(diac_hints)
        predictions, logits = self.diacritize_batch(
            char_inputs, diac_hints, input_lengths
        )
        output_sentences = []
        for length, src, prediction in zip(input_lengths, char_inputs, predictions):
            src = src[: length + 2]
            prediction = prediction[:length]
            sentence = self.text_encoder.combine_text_and_diacritics(
                list(src), list(prediction)
            )
            output_sentences.append(sentence)
        return output_sentences

    def diacritize_batch(self, char_inputs, diac_inputs, input_lengths):
        inputs = {
            "char_inputs": char_inputs,
            "diac_inputs": diac_inputs,
            "input_lengths": input_lengths,
        }
        indices, logits = self.session.run(None, inputs)
        return indices, logits


def numpy_pad_sequences(sequences, maxlen=None, value=0):
    """Pads a list of sequences to the same length using broadcasting.

    Args:
      sequences: A list of Python lists with variable lengths.
      maxlen: The maximum length to pad the sequences to. If not specified,
        the maximum length of all sequences in the list will be used.
      value: The value to use for padding (default 0).

    Returns:
      A numpy array with shape [batch_size, maxlen] where the sequences are padded
      with the specified value.
    """

    # Get the maximum length if not specified
    if maxlen is None:
        maxlen = max(len(seq) for seq in sequences)

    # Create a numpy array with the specified value and broadcast
    padded_seqs = np.full((len(sequences), maxlen), value)
    for i, seq in enumerate(sequences):
        padded_seqs[i, : len(seq)] = seq

    return padded_seqs


def extract_stack(stack, correct_reversed: bool = True):
    """
    Given stack, we extract its content to string, and check whether this string is
    available at all_possible_haraqat list: if not we raise an error. When correct_reversed
    is set, we also check the reversed order of the string, if it was not already correct.
    """
    char_haraqat = []
    while len(stack) != 0:
        char_haraqat.append(stack.pop())
    full_haraqah = "".join(char_haraqat)
    reversed_full_haraqah = "".join(reversed(char_haraqat))
    if full_haraqah in ALL_VALID_DIACRITICS:
        out = full_haraqah
    elif reversed_full_haraqah in ALL_VALID_DIACRITICS and correct_reversed:
        out = reversed_full_haraqah
    else:
        raise ValueError(
            f"""The letter has the following haraqat which are not found in valid diacritics: {'|'.join([ALL_VALID_DIACRITICS[diacritic]
                                         for diacritic in full_haraqah ])}"""
        )
    return out
