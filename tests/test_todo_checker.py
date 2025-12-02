from lib.todo_checker import *
import pytest

"""
Given a empty string 
It returns False
"""
def test_given_empty_string_returns_False():
    actual = check_notes("")
    expected = False
    assert actual == expected