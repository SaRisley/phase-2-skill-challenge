from lib.count_words import *

def test_count_four_words():
    result = count_words("This is four words")
    assert result == 4

def test_count_empty_string():
    result = count_words("")
    assert result == 0