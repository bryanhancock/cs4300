"""Tests for Task 4: Functions and Duck Typing."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

import pytest
from task4 import calculate_discount


# --- correct behaviour with various numeric types ---

@pytest.mark.parametrize("price, discount, expected", [
    (100,   20,   80.0),    # int / int
    (200.0, 25.0, 150.0),   # float / float
    (50,    10.0, 45.0),    # int / float
    (99.99, 0,    99.99),   # no discount
    (99.99, 100,  0.0),     # full discount
])
def test_calculate_discount_numeric_types(price, discount, expected):
    """Verify correct final price for various int/float combinations (duck typing)."""
    result = calculate_discount(price, discount)
    assert result == pytest.approx(expected, rel=1e-6)


# --- edge cases ---

def test_zero_price():
    """A price of 0 should always return 0.0 regardless of discount."""
    assert calculate_discount(0, 50) == 0.0


# --- input validation ---

def test_negative_price_raises():
    """A negative price should raise ValueError."""
    with pytest.raises(ValueError, match="non-negative"):
        calculate_discount(-10, 20)


@pytest.mark.parametrize("bad_discount", [-1, 101, 200])
def test_invalid_discount_raises(bad_discount):
    """A discount outside [0, 100] should raise ValueError."""
    with pytest.raises(ValueError, match="discount"):
        calculate_discount(100, bad_discount)


def test_non_numeric_price_raises():
    """A non-numeric price should raise TypeError."""
    with pytest.raises(TypeError):
        calculate_discount("free", 10)


def test_return_type_is_float():
    """calculate_discount should always return a float."""
    result = calculate_discount(100, 20)
    assert isinstance(result, float)
