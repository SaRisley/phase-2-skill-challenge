import pytest
from lib.exercise_one_est_reading_time import *

def test_estimated_reading_time_200_words():
    text = "hello \n"*199
    result = estimated_reading_time(text)
    assert result == 1

def test_estimated_reading_time_100_words():
    text = "hello \n"*99
    result = estimated_reading_time(text)
    assert result == 0.5

def test_estimated_reading_time_50_words():
    text = "hello \n"*49
    result = estimated_reading_time(text)
    assert result == 0.25

def test_estimated_reading_time_500_words():
    text = "hello \n"*499
    result = estimated_reading_time(text)
    assert result == 2.5

def test_estimated_reading_time_empty_string():
    text = ""
    result = estimated_reading_time(text)
    assert result == "Pick up a book!"

def test_estimated_reading_time_given_none():
    text = None
    with pytest.raises(Exception) as e:
        estimated_reading_time(text)
    error_message = str(e.value) 
    assert error_message == "No text given"
