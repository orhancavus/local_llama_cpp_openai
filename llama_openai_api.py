import requests

"""
This module provides functions to interact with a local LLaMA model via HTTP requests.

Functions:
    call_url_with_headers_and_data(url, headers, data):
        Sends an HTTP POST request to the specified URL with the given headers and JSON data.
        Returns the JSON response if the request is successful, otherwise returns an error message.

    get_result_content(prompt):
        Prepares the data payload and calls the LLaMA model endpoint to get a response for the given prompt.
        Returns the content of the response message.

    interact_with_llama():
        Initiates an interactive session with the LLaMA model, allowing the user to input prompts and receive responses.
        The session continues until the user inputs 'QUIT'.

Usage:
    Run this script directly to start an interactive session with the LLaMA model.
    Prior to running this script, ensure that the LLaMA model server is running and accessible at the specified URL.
    python api_like_OAI.py
"""
import json

LLM_URL = "http://127.0.0.1:8081/v1/chat/completions"


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


def get_result_content(prompt):
    # Define the URL, headers, and data
    url = LLM_URL
    headers = {"Content-Type": "application/json"}
    # TODO disable """### Human and ### Assistant """ expressions
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "n_predict": 512,
        "temperature": 0.2,
        "top_k": 40,
        "n_keep": 30,
        "top_p": 0.9,
    }
    # Call the function and store the result
    try:
        result = call_url_with_headers_and_data(url, headers, data)
        return result["choices"][0]["message"]["content"]
    except RuntimeError as e:
        return f"Connection error receiving LLM response : {e}"
    except json.JSONDecodeError as e:
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
        try:
            content = get_result_content(prompt)
            print(f"{content}")
        except requests.exceptions.RequestException as e:
            print(f"Connection error occured")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {str(e)}")
    print("End conversation ..\n\n")


if __name__ == "__main__":
    # content = get_result_content("How are you?")
    # print(f"Response :{content}")
    # write a script to call url with the specified hedear and data with the requests Python module
    interact_with_llama()
