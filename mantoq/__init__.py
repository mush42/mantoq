from .lib.buck import symbols
from .lib.buck.tokenization import (arabic_to_phonemes, phon_to_id_,
                                    phonemes_to_tokens, simplify_phonemes)
from .lib.buck.tokenization import tokens_to_ids as _tokens_to_id
from .num2words import num2words
from .tashkeel import tashkeel

MANTOQ_SYMBOLS = dict(phon_to_id_)
MANTOQ_SPECIAL_SYMBOLS = dict(
    pad=phon_to_id_[symbols.PADDING_TOKEN],
    eos=phon_to_id_[symbols.EOS_TOKEN],
)
# Maps Arabic-specific puncs with their English equivlents
AR_SPECIAL_PUNCS_TABLE = str.maketrans("،؟؛", ",?;")
OMITTED_SYMBOLS = str.maketrans("", "", "+=<>")

# Quotes
QUOTES = '“”„«»'
QUOTES_TABLE = str.maketrans(QUOTES, '"' * len(QUOTES))
BRACKETS_TABLE = str.maketrans("[]{}", "()()")


def g2p(
    text: str,
    add_tashkeel: bool = True,
    process_numbers: bool = True,
    append_eos: bool = False,
) -> list[str]:
    text = text.translate(AR_SPECIAL_PUNCS_TABLE).translate(QUOTES_TABLE).translate(BRACKETS_TABLE)
    if add_tashkeel:
        text = tashkeel(text)
    if process_numbers:
        text = num2words(text)
    normalized_text = text
    phones = arabic_to_phonemes(text)
    phones = simplify_phonemes(phones)
    tokens = phonemes_to_tokens(phones)
    if not append_eos:
        tokens = tokens[:-1]
    return normalized_text, tokens


def tokens2ids(tokens: list[str]) -> list[int]:
    return _tokens_to_id(tokens)
