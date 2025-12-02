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

"""
Given a string without '#TODO' 
It returns False
"""
def test_given_string_without_hashtag_TODO_returns_False():
    actual_one = check_notes("Finish the challenge")
    actual_two  = check_notes("#todo Finish the challenge")
    expected = False
    assert expected == actual_one
    assert expected == actual_two

"""
Given a parameter that is not a string
Raise a TypeError message "Only strings allowed!"
check_notes(3) => raises TypeError "Only strings allowed!"
"""
def test_given_not_string_raises_type_error():
    with pytest.raises(TypeError) as error:
        check_notes(1)
    actual = str(error.value)
    expected = "Only strings allowed!"
    assert actual == expected