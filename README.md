<div align="center">

[![python](https://img.shields.io/badge/-Python_3.9-blue?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3100/)

</div>

<div align="center">

# Mantoq: Arabic Grapheme-to-Phoneme (G2P) Conversion

**Mantoq** is a Python package designed for Arabic Grapheme-to-Phoneme (G2P) conversion, which is the process of converting written Arabic text into phonetic representations. This can be useful for various applications such as speech synthesis, natural language processing, and more.

</div>

## Installation

To install the Mantoq package directly from GitHub, follow these steps:

1. **Clone the repository**: If you haven't already, clone the repository from GitHub.

   ```bash
   git clone https://github.com/mush42/mantoq.git
   cd mantoq
   ```

2. **Install the package**: Install the package using `pip` with the `-e` flag, which allows you to install it in "editable" mode. This way, you can sync changes as you update the repository.

   ```bash
   uv sync
   ```

## Public Interface

### `g2p(text: str, add_tashkeel: bool = True, process_numbers: bool = True, append_eos: bool = False) -> list[str]`

Converts Arabic text to phonemes and returns a list of tokens.

- `text`: The Arabic text to be converted.
- `add_tashkeel`: (Optional) Whether to add tashkeel (diacritics) to the text. Default is `True`.
- `process_numbers`: (Optional) Whether to process numeric values in the text. Default is `True`.
- `append_eos`: (Optional) Whether to append the end-of-sequence (EOS) token. Default is `False`.

**Example Usage:**

```python
import mantoq

tokens = mantoq.g2p("مرحبا بالعالم")
print(tokens)
```

### `tokens_to_ids(tokens: list[str]) -> list[int]`

Converts a list of tokens into their corresponding integer IDs.

- `tokens`: A list of tokens to be converted.

**Example Usage:**

```python
import mantoq

token_ids = mantoq.tokens_to_ids(["m", "a", "r", "h", "a", "b", "a"])
print(token_ids)
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
