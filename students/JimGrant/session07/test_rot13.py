from rot13 import rot13


def test_validation():
    assert(rot13(None) is None)
    assert(rot13(1) is None)
    assert(rot13("") == "")


def test_lower_case():
    assert(rot13("abcd") == "nopq")
    assert(rot13("nopq") == "abcd")


def test_upper_case():
    assert(rot13("EFGH") == "RSTU")
    assert(rot13("RSTU") == "EFGH")


def test_mixed_case():
    assert(rot13("Python") == "Clguba")


def test_punctuation():
    assert(rot13("We're knights of the Round Table!") ==
           "Jr'er xavtugf bs gur Ebhaq Gnoyr!")
    assert(rot13("Jr'er xavtugf bs gur Ebhaq Gnoyr!") ==
           "We're knights of the Round Table!")
