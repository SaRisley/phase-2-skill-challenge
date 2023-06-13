# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimated_reading_time(text):
    """Returns estimated reading time for text assuming the user reads 200 words per min

    Parameters: (list all parameters and their types)
        text: a string containing words

    Returns: (state the return value and its type)
        a string with a float to 2 decimal places representing mins (eg. 2 == 2 mins, 0.5 == 30secs)
        eg.
        "This will take you X minutes to read"

    Side effects: (state any side effects)
        This function doesn't have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a 400 word text the  function will return 2
"""
estimated_reading_time(text) => 2

"""
Given a 100 word text the  function will return 0.5
"""
estimated_reading_time(text) => 0.5

"""
Given an empty string
It returns "Pick up a book!"
"""
estimated_reading_time("") => "Pick up a book!"

"""
Given a None value
It throws an error
"""
estimated_reading_time(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.exercise_one_est_reading_time import *

"""
Returns estimated reading time for text assuming the user reads 200 words per min
"""
def test_estimated_reading_time():
    text_len_200 = "hello\n"*10
    result = estimated_reading_time(text_len_200)
    assert result == 0.5

```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->