"""
Tests for the Meme Flask application.
"""
import pytest
from unittest.mock import patch, MagicMock
from app import app, meme_get


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_route_exists(client):
    """Test that the index route exists and returns 200."""
    with patch('app.meme_get') as mock_meme_get:
        mock_meme_get.return_value = ("https://example.com/meme.jpg", "funny")
        response = client.get('/')
        assert response.status_code == 200


def test_index_route_contains_meme(client):
    """Test that the index route returns HTML with meme content."""
    with patch('app.meme_get') as mock_meme_get:
        mock_meme_get.return_value = ("https://example.com/meme.jpg", "funny")
        response = client.get('/')
        assert b'https://example.com/meme.jpg' in response.data or b'meme' in response.data.lower()


@patch('app.requests.request')
def test_meme_get_function(mock_request):
    """Test the meme_get function."""
    # Mock the API response
    mock_response = MagicMock()
    mock_response.text = '{"preview": ["small", "medium", "large"], "subreddit": "memes"}'
    mock_request.return_value = mock_response

    meme_large, subreddit = meme_get()

    # The function uses preview[-2] which is the second-to-last element
    assert meme_large == "medium"
    assert subreddit == "memes"
    mock_request.assert_called_once_with("GET", "https://meme-api.com/gimme")


def test_app_exists():
    """Test that the Flask app exists."""
    assert app is not None


def test_app_is_flask_instance():
    """Test that app is a Flask instance."""
    from flask import Flask
    assert isinstance(app, Flask)
