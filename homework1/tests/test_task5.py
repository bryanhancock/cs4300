"""Tests for Task 5: Lists and Dictionaries."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

import pytest
from task5 import (
    FAVORITE_BOOKS,
    get_first_three_books,
    STUDENT_DATABASE,
    get_student_id,
    add_student,
)


# --- book list ---

def test_book_list_has_five_entries():
    """FAVORITE_BOOKS should contain exactly 5 books."""
    assert len(FAVORITE_BOOKS) == 5


def test_each_book_has_title_and_author():
    """Every book entry must have a 'title' and an 'author' key."""
    for book in FAVORITE_BOOKS:
        assert "title" in book
        assert "author" in book


def test_get_first_three_books_length():
    """List slice should return exactly 3 books."""
    result = get_first_three_books()
    assert len(result) == 3


def test_get_first_three_books_matches_source():
    """Sliced list should match the first three entries of FAVORITE_BOOKS."""
    assert get_first_three_books() == FAVORITE_BOOKS[:3]


# --- student database ---

def test_student_database_not_empty():
    """Student database should contain at least one entry."""
    assert len(STUDENT_DATABASE) > 0


@pytest.mark.parametrize("name, expected_id", [
    ("Alice",   10001),
    ("Bob",     10002),
    ("Charlie", 10003),
    ("Diana",   10004),
])
def test_get_student_id_known(name, expected_id):
    """get_student_id should return the correct ID for known students."""
    assert get_student_id(name) == expected_id


def test_get_student_id_unknown():
    """get_student_id should return None for unknown students."""
    assert get_student_id("Nobody") is None


def test_add_student():
    """add_student should insert a new student into the database."""
    add_student("Eve", 10005)
    assert get_student_id("Eve") == 10005
    # Clean up so other tests are not affected
    del STUDENT_DATABASE["Eve"]
