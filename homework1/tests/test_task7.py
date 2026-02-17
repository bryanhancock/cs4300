"""Tests for Task 7: Package Management (requests library).

All HTTP calls are mocked so tests pass without network access.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

import pytest
from unittest.mock import patch, MagicMock
import requests

from task7 import fetch_post, fetch_posts


# ── helpers ────────────────────────────────────────────────────────────────

def _make_response(json_data, status_code=200):
    """Build a minimal mock requests.Response."""
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.json.return_value = json_data
    # raise_for_status raises only on 4xx/5xx
    if status_code >= 400:
        mock_resp.raise_for_status.side_effect = requests.HTTPError(
            response=mock_resp
        )
    else:
        mock_resp.raise_for_status.return_value = None
    return mock_resp


FAKE_POST = {"userId": 1, "id": 1, "title": "Test Title", "body": "Test body."}
FAKE_POSTS = [
    {"userId": 1, "id": i, "title": f"Title {i}", "body": f"Body {i}."}
    for i in range(1, 11)
]


# ── fetch_post ─────────────────────────────────────────────────────────────

@patch("task7.requests.get")
def test_fetch_post_returns_dict(mock_get):
    """fetch_post should return a dict with the expected keys."""
    mock_get.return_value = _make_response(FAKE_POST)
    result = fetch_post(1)
    assert isinstance(result, dict)
    assert result["id"] == 1
    assert result["title"] == "Test Title"


@patch("task7.requests.get")
def test_fetch_post_calls_correct_url(mock_get):
    """fetch_post should call the correct URL."""
    mock_get.return_value = _make_response(FAKE_POST)
    fetch_post(1)
    called_url = mock_get.call_args[0][0]
    assert called_url.endswith("/posts/1")


@patch("task7.requests.get")
def test_fetch_post_http_error(mock_get):
    """fetch_post should propagate HTTPError on non-2xx responses."""
    mock_get.return_value = _make_response({}, status_code=404)
    with pytest.raises(requests.HTTPError):
        fetch_post(999)


@pytest.mark.parametrize("bad_id", [0, -1, "one", 3.5, None])
def test_fetch_post_invalid_id(bad_id):
    """fetch_post should raise ValueError for non-positive-integer post_ids."""
    with pytest.raises(ValueError, match="positive integer"):
        fetch_post(bad_id)


# ── fetch_posts ────────────────────────────────────────────────────────────

@patch("task7.requests.get")
def test_fetch_posts_default_limit(mock_get):
    """fetch_posts with default limit=5 should return at most 5 items."""
    mock_get.return_value = _make_response(FAKE_POSTS)
    result = fetch_posts()
    assert len(result) == 5


@patch("task7.requests.get")
def test_fetch_posts_custom_limit(mock_get):
    """fetch_posts should respect a custom limit."""
    mock_get.return_value = _make_response(FAKE_POSTS)
    result = fetch_posts(3)
    assert len(result) == 3


@patch("task7.requests.get")
def test_fetch_posts_returns_list(mock_get):
    """fetch_posts should always return a list."""
    mock_get.return_value = _make_response(FAKE_POSTS)
    result = fetch_posts()
    assert isinstance(result, list)
