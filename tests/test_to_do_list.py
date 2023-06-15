import pytest
from lib.to_do_list import *

def test_list_one_to_dos():
    to_dos = ToDoList()
    to_dos.add_to_do("Walk the dog")
    result = to_dos.list_to_dos()
    assert result == ["Walk the dog"]

def test_list_multi_to_dos():
    to_dos = ToDoList()
    to_dos.add_to_do("Walk the dog")
    to_dos.add_to_do("Water the plants")
    result = to_dos.list_to_dos()
    assert result == ["Walk the dog", "Water the plants"]

def test_empty_list_of_to_dos():
    to_dos = ToDoList()
    with pytest.raises(Exception) as e:
        to_dos.list_to_dos()
    error_message = str(e.value) 
    assert error_message == "Nothing to do!"
