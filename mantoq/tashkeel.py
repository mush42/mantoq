import warnings

from .lib.pylibtashkeel import LibtashkeelDiacritizer

try:
    import onnxruntime

    _TASHKEEL_AVAILABLE = True
except ImportError:
    _TASHKEEL_AVAILABLE = False

_DIACRITIZER_INST = None


def tashkeel(text: str) -> str:
    global _DIACRITIZER_INST
    if not _TASHKEEL_AVAILABLE:
        warnings.warn(
            "Warning: The Tashkeel feature will not be available. Please re-install with the `libtashkeel` extra.",
            UserWarning,
        )
        return text
    if _DIACRITIZER_INST is None:
        _DIACRITIZER_INST = LibtashkeelDiacritizer()
    return _DIACRITIZER_INST([text])[0]
