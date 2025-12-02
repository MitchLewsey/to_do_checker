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

"""
Given a string with '#TODO' 
It returns True
"""
def test_given_string_with_hashtag_TODO_returns_True():
    actual = check_notes("#TODO finish the challenge")
    expected = True
    assert actual == expected