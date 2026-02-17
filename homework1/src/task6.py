"""Task 6: File Handling — read a file and count its words."""
import os


def count_words(filepath: str) -> int:
    """
    Read the file at *filepath* and return the total number of words.

    A 'word' is any whitespace-separated token (same behaviour as str.split()).

    Args:
        filepath: Absolute or relative path to the text file.

    Returns:
        Integer word count.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, "r", encoding="utf-8") as fh:
        content = fh.read()

    return len(content.split())


if __name__ == "__main__":
    # Resolve path relative to this script's location so it works from
    # any working directory.
    readme_path = os.path.join(os.path.dirname(__file__), "..", "task6_read_me.txt")
    readme_path = os.path.normpath(readme_path)
    word_count = count_words(readme_path)
    print(f"Word count in task6_read_me.txt: {word_count}")
