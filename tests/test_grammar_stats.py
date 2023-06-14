import pytest
from lib.grammar_stats import *

def test_starts_with_cap():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello!")
    assert result == True

def test_ends_with_punc():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello!")
    assert result == True

def test_starts_with__no_cap():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello!")
    assert result == False

def test_ends_with_no_punc():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello")
    assert result == False

def test_is_all_punc():
    grammar_stats = GrammarStats()
    result = grammar_stats.check(".?!")
    assert result == False

def test_is_empty_string():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("")
    error_message = str(e.value) 
    assert error_message == "Empty string"

def test_is_none():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check(None)
    error_message = str(e.value) 
    assert error_message == "No text given"

def test_percentage_good_100():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello!")
    result = grammar_stats.percentage_good()
    assert result == 100

def test_percentage_good_0():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello")
    result = grammar_stats.percentage_good()
    assert result == 0

