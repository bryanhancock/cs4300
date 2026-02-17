"""Tests for Task 1: Hello World."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from task1 import hello_world


def test_hello_world_output(capsys):
    """Verify that hello_world prints 'Hello, World!' to stdout."""
    hello_world()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"


def test_hello_world_return():
    """Verify that hello_world returns the correct string."""
    result = hello_world()
    assert result == "Hello, World!"
