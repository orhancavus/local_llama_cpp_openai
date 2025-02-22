import requests
import json

"""
This module provides functions to interact with a local LLM (Language Model) server.

Functions:
    call_url_with_headers_and_data(url, headers, data):
        Sends an HTTP POST request to the specified URL with the given headers and JSON data.
        Returns the JSON response if the request is successful, otherwise returns an error message.

    sample_usage():
        Demonstrates a sample usage of the call_url_with_headers_and_data function by sending a predefined prompt to the LLM server.

    get_result_content(prompt):
        Sends a prompt to the LLM server and returns the generated content.
        Configures various parameters for the LLM request such as temperature, stop sequence, top_k, n_keep, and top_p.

    interact_with_llama():
        Starts an interactive session with the LLM server, allowing the user to input prompts and receive responses until "QUIT" is entered.

Usage:
    Run this script directly to start an interactive session with the LLM server.
    Prior to running this script, ensure that the LLM server is running and accessible at the specified URL.
   ./server -c 4096 --host 0.0.0.0 -t 16 --mlock -m ../TheBloke/Mistral-7B-Instruct-v0.1-GGUF/mistral-7b-instruct-v0.1.Q4_K_S.gguf    
"""

LLM_URL = "http://localhost:8080/completion"


def call_url_with_headers_and_data(url, headers, data):
    try:
        # Send an HTTP POST request with headers and JSON data
        response = requests.post(url, headers=headers, json=data)

        # Check the response status code
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Return the JSON response
        return response.json()

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"An error occurred calling the URL: {url}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON response: {str(e)}") from e


def sample_usage():
    # Define the URL, headers, and data
    url = LLM_URL
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": "Building a website can be done in 10 simple steps:",
        "n_predict": 128,
    }

    # Call the function and store the result
    result = call_url_with_headers_and_data(url, headers, data)

    # Print the result
    print(result["content"])


def get_result_content(prompt):
    # Define the URL, headers, and data
    url = LLM_URL
    headers = {"Content-Type": "application/json"}
    # TODO disable """### Human and ### Assistant """ expressions
    data = {
        "prompt": prompt,
        "n_predict": 512,
        "temperature": 0.2,
        "stop": "['\n### Human:']",
        "top_k": 40,
        "n_keep": 30,
        "top_p": 0.9,
    }
    try:
        # Call the function and store the result
        result = call_url_with_headers_and_data(url, headers, data)
        return result["content"]
    except RuntimeError as e:
        return f"Connection error receiving LLM response : {e}"
    except ValueError as e:
        return f"Error decoding JSON response: {str(e)}"


def interact_with_llama():
    # Start and continue interaction with llma until QUIT is entered
    continue_interaction = True
    print("Start conversation ..\n\n")
    while continue_interaction:
        prompt = input("Prompt:")
        if prompt == "QUIT":
            continue_interaction = False
            break
        print(f">Prompt   : {prompt}")
        print(f">Response : ", end="")
        content = get_result_content(prompt)
        print(f"{content}")
    print("End conversation ..\n\n")


if __name__ == "__main__":
    interact_with_llama()
