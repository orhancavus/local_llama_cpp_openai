import requests
import argparse

"""
This script demonstrates how to make a request to a locally hosted language model API
that follows the OpenAI API format. It sends a prompt to the model and prints the response.

Functions:
    sample_usage(prompt: str) -> str:
        Sends a prompt to the local LLM API and returns the model's response.

Usage:
    Run the script directly to see a sample usage of the local LLM API.
"""

LLM_URL = "http://127.0.0.1:8081/v1/chat/completions"


def sample_usage(prompt):
    # Define the URL, headers, and data
    url = LLM_URL
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        result_json = response.json()
        return result_json["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"An error occurred, for connection errors run <python api_like_OAI.py>:"


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Send a prompt to the local LLM API and get a response."
    )
    parser.add_argument(
        "prompt",
        type=str,
        nargs="?",
        default="Say this is a test!",
        help="The prompt to send to the LLM",
    )
    args = parser.parse_args()

    completion = sample_usage(args.prompt)

    print("\nSample Local LLM with OpenAI format usage:\n")
    print(f"Prompt: {args.prompt}")
    print(completion)
