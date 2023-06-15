import pytest
from lib.complete_to_list import *

def test_task_marked_completed():
    to_do_list = ToDoList()
    result = to_do_list.mark_as_complete("Walk the dog")
    assert result == ["Water the plants", "Walk the dog COMPLETED"]


def test_completed_task_removed():
    to_do_list = ToDoList()
    to_do_list.mark_as_complete("Walk the dog")
    result = to_do_list.remove_completed_task()
    assert result == ["Water the plants"]