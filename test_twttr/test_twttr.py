from twttr import shorten

def test_shorten_lowercase():
    assert shorten("cat") == "ct"
    assert shorten("house") == "hs"

def test_shorten_uppercase():
    assert shorten("MAN") == "MN"
    assert shorten("CAmERA") == "CmR"

def test_shorten_numbers():
    assert shorten("3hours") == "3hrs"

def test_shorten_punctuation():
    assert shorten("T-way?") == "T-wy?"
