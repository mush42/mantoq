from mantoq import g2p


def test_basic():
    phonemes = g2p("بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ")
    assert phonemes == ['b', 'i', 's', 'm', 'i', '_+_', 'l', '_dbl_', 'a', 'h', 'i', '_+_', 'r', '_dbl_', 'a', 'H', 'm', 'a', 'n', 'i', '_+_', 'r', '_dbl_', 'a', 'H', 'i', '_dbl_', 'm', 'i']
