from lib.make_snippet import *

def test_over_five_words():
    result = make_snippet("This is going to be over five")
    assert result == "This is going to be ..."

def test_less_than_five():
    result = make_snippet("less than five")
    assert result == "less than five"