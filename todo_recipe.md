# 'Check to do in notes' Function Design Recipe

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._
-def check_notes(notes):
    returns true or false
-parameters: 1 string
-returns true/false
-no side effects

```python
# EXAMPLE

def check_notes(notes):
    """Checkes the notes and returns true if it includes #TODO else false

    Parameters: (list all parameters and their types)
        notes: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a boolean (True or False)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a empty string 
It returns False
"""
check_notes("") => False

"""
Given a string with '#TODO' it returns True
"""
check_notes("#TODO finish the challenge") => True

"""
Given a string without '#TODO' returns False
"""
check_notes("Finish the challenge") => False
check_notes("#todo Finish the challenge") => False

"""
Given a parameter that is not a string
Raise a TypeError message "Only strings allowed!"
"""
check_notes(3) => raises TypeError "Only strings allowed!"

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!