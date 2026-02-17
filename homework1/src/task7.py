"""
Task 7: Package Management — using the 'requests' library.

Demonstrates fetching data from a public REST API (JSONPlaceholder).
"""
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_post(post_id: int) -> dict:
    """
    Fetch a single post by ID from the JSONPlaceholder API.

    Args:
        post_id: The ID of the post to fetch (1-based).

    Returns:
        A dict containing the post's userId, id, title, and body.

    Raises:
        ValueError:           If post_id is not a positive integer.
        requests.HTTPError:   If the server returns a non-2xx status.
    """
    if not isinstance(post_id, int) or post_id < 1:
        raise ValueError("post_id must be a positive integer.")

    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def fetch_posts(limit: int = 5) -> list[dict]:
    """
    Fetch multiple posts (up to *limit*) from the JSONPlaceholder API.

    Args:
        limit: Maximum number of posts to return (default 5).

    Returns:
        A list of post dicts.
    """
    url = f"{BASE_URL}/posts"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()[:limit]


if __name__ == "__main__":
    post = fetch_post(1)
    print("Single post:")
    print(f"  ID     : {post['id']}")
    print(f"  Title  : {post['title']}")
    print(f"  User   : {post['userId']}")

    print("\nFirst 3 posts:")
    for p in fetch_posts(3):
        print(f"  [{p['id']}] {p['title']}")
