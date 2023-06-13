import pytest
from lib.improve_grammar import *

def test_starts_with_cap():
    result = improve_grammar("Hello!")
    assert result == True

def test_ends_with_punc():
    result = improve_grammar("Hello!")
    assert result == True

def test_starts_with__no_cap():
    result = improve_grammar("hello!")
    assert result == False

def test_ends_with_no_punc():
    result = improve_grammar("Hello")
    assert result == False

def test_is_all_punc():
    result = improve_grammar(".?!")
    assert result == False

def test_is_empty_string():
    result = improve_grammar("")
    assert result == False

def test_is_none():
    with pytest.raises(Exception) as e:
        improve_grammar(None)
    error_message = str(e.value) 
    assert error_message == "No text given"
