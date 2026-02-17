"""Tests for Task 6: File Handling."""
import sys
import os
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

import pytest
from task6 import count_words

# Path to the provided readme file (one directory above tests/)
README_PATH = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "task6_read_me.txt")
)


# --- task6_read_me.txt ---

def test_readme_word_count():
    """Verify the word count of task6_read_me.txt is 104."""
    assert count_words(README_PATH) == 104


# --- parametrized tests with temporary files ---

@pytest.mark.parametrize("content, expected_count", [
    ("Hello World",                    2),
    ("one two three four five",        5),
    ("  lots   of   whitespace   ",    3),
    ("single",                         1),
    ("",                               0),
    ("line one\nline two\nline three", 6),
])
def test_count_words_various_inputs(content, expected_count, tmp_path):
    """
    Parametrized test: write content to a temp file and verify word count.
    Uses pytest's built-in tmp_path fixture so no manual cleanup is needed.
    """
    temp_file = tmp_path / "sample.txt"
    temp_file.write_text(content, encoding="utf-8")
    assert count_words(str(temp_file)) == expected_count


# --- error handling ---

def test_missing_file_raises():
    """count_words should raise FileNotFoundError for a non-existent path."""
    with pytest.raises(FileNotFoundError):
        count_words("/tmp/this_file_does_not_exist_xyz.txt")
