import requests
import json

# Define the URL, headers, and data
url = "http://localhost:8080/completion"
headers = {"Content-Type": "application/json"}
data = {
    "prompt": "Building a website can be done in 10 simple steps:",
    "n_predict": 128,
}

try:
    # Send an HTTP POST request with headers and JSON data
    response = requests.post(url, headers=headers, json=data)

    # Check the response status code
    if response.status_code == 200:
        # Print the JSON response
        print(response.json())
    else:
        print(f"HTTP Request Failed with Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {str(e)}")
