"""Tests for Task 2: Variables and Data Types."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

import pytest
from task2 import get_integer, get_float, get_string, get_boolean


@pytest.mark.parametrize("func, expected_type, expected_value", [
    (get_integer, int,   42),
    (get_float,   float, 3.14),
    (get_string,  str,   "Python Programming"),
    (get_boolean, bool,  True),
])
def test_data_types(func, expected_type, expected_value):
    """Verify return type and value for each data type function."""
    result = func()
    assert isinstance(result, expected_type), (
        f"Expected type {expected_type}, got {type(result)}"
    )
    assert result == expected_value, (
        f"Expected {expected_value}, got {result}"
    )
