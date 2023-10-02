import pytest
from unittest.mock import Mock, patch
import simple_call  # Import the script you want to test


@patch("simple_call.requests.post")
def test_sample_usage(mock_post):
    # Prepare a mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "choices": [{"message": {"content": "Generated completion"}}]
    }
    mock_post.return_value = mock_response

    # Call the function with a sample prompt
    completion = simple_call.sample_usage("This is a test prompt")

    # Assertions
    assert completion == "Generated completion"


if __name__ == "__main__":
    pytest.main()
