from mantoq import g2p


def test_basic():
    _normalized_text, phonemes = g2p("بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ")
    assert phonemes == ['b', 'i', 's', 'm', 'i', '_+_', 'llll', 'a', 'a', 'h', 'i', '_+_', 'rrrr', 'a', 'a', 'H', 'm', 'a', 'a', 'n', 'i', '_+_', 'rrrr', 'a', 'a', 'H', 'i', '_dbl_', 'm', 'i']


def test_with_numbs():
    _normalized_text, phonemes = g2p("وقد حضر اللقاء 3734 فردا.")
    # TODO @mush42: investigate added 'a' at the end
    assert phonemes == ['w', 'a', 'q', 'a', 'd', '_+_', 'H', 'a', 'D', 'a', 'r', 'a', '_+_', 'l', '_dbl_', 'i', 'q', 'aa', '<', 'u', '_+_', '^', 'a', 'l', 'aa', '^', '_+_', '<', 'aa', 'l', '<', 'a', 'f', '_+_', 'u', '_dbl_', '_+_', 's', 'a', 'b', 'E', 'm', 'i', '<', 'a', '_+_', 'u', '_dbl_', '_+_', '<', 'a', 'r', 'b', 'a', 'E', '_+_', 'u', '_dbl_', '_+_', '^', 'a', 'l', 'aa', '^', 'u', '_dbl_', 'n', 'a', '_+_', 'f', 'r', 'd', 'aa', '.', '_+_', 'a']