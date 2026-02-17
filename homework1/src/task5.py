"""Task 5: Lists and Dictionaries."""


# A list of favorite books: each entry is a dict with title and author.
FAVORITE_BOOKS = [
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt & David Thomas"},
    {"title": "Clean Code",               "author": "Robert C. Martin"},
    {"title": "Fluent Python",            "author": "Luciano Ramalho"},
    {"title": "Design Patterns",          "author": "Gang of Four"},
    {"title": "You Don't Know JS",        "author": "Kyle Simpson"},
]


def get_first_three_books() -> list[dict]:
    """Return the first three books using list slicing."""
    return FAVORITE_BOOKS[:3]


# A simple student database: maps student name -> student ID.
STUDENT_DATABASE: dict[str, int] = {
    "Alice":   10001,
    "Bob":     10002,
    "Charlie": 10003,
    "Diana":   10004,
}


def get_student_id(name: str) -> int | None:
    """Return the student ID for a given name, or None if not found."""
    return STUDENT_DATABASE.get(name)


def add_student(name: str, student_id: int) -> None:
    """Add a new student to the database."""
    STUDENT_DATABASE[name] = student_id


if __name__ == "__main__":
    print("First 3 books:")
    for book in get_first_three_books():
        print(f"  {book['title']} by {book['author']}")

    print("\nStudent database:")
    for name, sid in STUDENT_DATABASE.items():
        print(f"  {name}: {sid}")
