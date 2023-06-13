import pytest
from lib.check_to_do import *

def test_check_to_do_incl():
    result = check_to_do("#TODO walk the dog")
    assert result == ["#TODO walk the dog"]

def test_if_no_todo():
    result = check_to_do("walk the dog")
    assert result == []

def test_if_none():
    with pytest.raises(Exception) as e:
        check_to_do(None)
    error_message = str(e.value)
    assert error_message == "Nothing provided"

def test_if_empty_string():
    result = check_to_do("")
    assert result == []