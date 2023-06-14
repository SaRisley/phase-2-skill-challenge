import pytest
from lib.diary_entry import *

def test_formatted_diary():
    diary_entry = DiaryEntry("Today", "Learn to code")
    result = diary_entry.format()
    assert result == "Today: Learn to code"

def test_count_words():
    diary_entry = DiaryEntry("Today", "Learn to code")
    result = diary_entry.count_words()
    assert result == 4

def test_reading_time():
    diary_entry = DiaryEntry("Today", "Learn to code")
    result = diary_entry.reading_time(40)
    assert result == 0.1

def test_reading_chunk():
    diary_entry = DiaryEntry("Today", "Learn to code")
    result = diary_entry.reading_chunk(4, 1)
    assert result == "Today: Learn to code"

def test_reading_chunk_1wpm():
    diary_entry = DiaryEntry("Today", "Learn to code")
    result = diary_entry.reading_chunk(1, 1)
    assert result == "Today:"

def test_repeated_reading_chunk():
    diary_entry = DiaryEntry("Today", "Learn to code")
    with pytest.raises(Exception) as e:
        diary_entry.reading_chunk(4, 1)
    error_message = str(e.value) 
    assert error_message == "You've already read this!"
