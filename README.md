<div align="center">

[![python](https://img.shields.io/badge/-Python_3.11-blue?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3110/)

</div>

<div align="center">

# Mantoq: Arabic Grapheme-to-Phoneme (G2P) Conversion

**Mantoq** is a Python package designed for Arabic Grapheme-to-Phoneme (G2P) conversion, which is the process of converting written Arabic text into phonetic representations. This can be useful for various applications such as speech synthesis, natural language processing, and more.

</div>

## Installation

To install the Mantoq package directly from GitHub, follow these steps:

1. **Clone the repository**:

If you haven't already, clone the repository from GitHub.

   ```bash
   git clone https://github.com/mush42/mantoq.git
   ```

2. **Install the package**:

We recommend using [uv](https://docs.astral.sh/uv/getting-started/installation/) to install the package:

   ```bash
   cd mantoq
   uv sync
   ```

## Public Interface

### G2P

```python
mantoq.g2p(text: str, add_tashkeel: bool = True, process_numbers: bool = True, append_eos: bool = False) -> list[str]
```

Converts Arabic text to phonemes and returns a list of tokens.

- `text`: The Arabic text to be converted.
- `add_tashkeel`: (Optional) Whether to add tashkeel (diacritics) to the text. Default is `True`.
- `process_numbers`: (Optional) Whether to process numeric values in the text. Default is `True`.
- `append_eos`: (Optional) Whether to append the end-of-sequence (EOS) token. Default is `False`.

**Example Usage:**

```python
import mantoq

normalized_text, phonemes = mantoq.g2p("مرحبا بالعالم")
print(normalized_text)
# مَرْحَبًا بِالْعالَمِ
print(phonemes)
# ['m', 'a', 'r', 'H', 'a', 'b', 'a', 'n', 'aa', '_+_', 'b', 'i', 'l', 'E', 'aa', 'l', 'a', 'm', 'i']
```

### Tokens to IDs

```python
mantoq.tokens2ids(tokens: list[str]) -> list[int]
```

Converts a list of tokens into their corresponding integer IDs.

- `tokens`: A list of tokens to be converted.

**Example Usage:**

```python
import mantoq

token_ids = mantoq.tokens2ids(['m', 'a', 'r', 'H', 'a', 'b', 'a', 'n', 'aa', '_+_', 'b', 'i', 'l', 'E', 'aa', 'l', 'a', 'm', 'i'])
print(token_ids)
# [37, 43, 23, 19, 43, 15, 43, 38, 46, 4, 15, 45, 36, 31, 46, 36, 43, 37, 45]
```

## Acknowledgements

**Mantoq** uses code from the following repositories:

- [Libtashkeel](https://github.com/mush42/libtashkeel/): for diacritic restoration model and logic.
- [tts-arabic-pytorch](https://github.com/nipponjo/tts-arabic-pytorch): for the Buckwalter transliteration code.
- [PyArabic](https://github.com/linuxscout/pyarabic/): for num2words and some utilities.
- [diacritization_evaluation](https://github.com/almodhfer/diacritization_evaluation): for diacritic extraction Algorithm and code.

## Contributing

Contributions are welcome! If you'd like to contribute to Mantoq, please fork the repository, make your changes, and submit a pull request.

## License

Copyright (c) Musharraf Omer. Mantoq is licensed under the MIT License. See [LICENSE](./LICENSE) for more details.
