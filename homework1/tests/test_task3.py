"""Tests for Task 3: Control Structures."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

import pytest
from task3 import check_sign, first_n_primes, sum_one_to_n


# --- check_sign ---

@pytest.mark.parametrize("number, expected", [
    (10,   "positive"),
    (0.5,  "positive"),
    (-3,   "negative"),
    (-0.1, "negative"),
    (0,    "zero"),
])
def test_check_sign(number, expected):
    """Verify sign detection for positive, negative, and zero inputs."""
    assert check_sign(number) == expected


# --- first_n_primes ---

def test_first_10_primes():
    """Verify the first 10 prime numbers are correct."""
    assert first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_first_prime_only():
    """Edge case: only the first prime."""
    assert first_n_primes(1) == [2]


def test_zero_primes():
    """Edge case: requesting zero primes returns an empty list."""
    assert first_n_primes(0) == []


# --- sum_one_to_n ---

def test_sum_1_to_100():
    """Verify the sum from 1 to 100 equals 5050."""
    assert sum_one_to_n(100) == 5050


@pytest.mark.parametrize("n, expected", [
    (1,  1),
    (5,  15),
    (10, 55),
])
def test_sum_various(n, expected):
    """Verify sum for various upper bounds."""
    assert sum_one_to_n(n) == expected
