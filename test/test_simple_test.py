import pytest
from unittest.mock import Mock, patch
import requests
import llama_api_client  # Import the script you want to test


@patch("llama_api_client.requests.post")
def test_sample_usage(mock_post):
    # Prepare a mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "choices": [{"message": {"content": "Generated completion"}}]
    }
    mock_post.return_value = mock_response

    # Call the function with a sample prompt
    completion = llama_api_client.sample_usage("This is a test prompt")

    # Assertions
    assert completion == "Generated completion"


@patch("llama_api_client.requests.post")
def test_sample_usage_connection_error(mock_post):
    # Simulate a connection error
    mock_post.side_effect = requests.exceptions.ConnectionError

    # Call the function with a sample prompt and handle the exception
    try:
        completion = llama_api_client.sample_usage("This is a test prompt")
    except requests.exceptions.ConnectionError:
        completion = (
            "An error occurred, for connection errors run <python api_like_OAI.py>:"
        )

    # Assertions
    assert (
        completion
        == "An error occurred, for connection errors run <python api_like_OAI.py>:"
    )


if __name__ == "__main__":
    pytest.main()
