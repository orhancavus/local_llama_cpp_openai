import requests
import json

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

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    return result


if __name__ == "__main__":
    prompt = "Say this is a test!"
    result_json = sample_usage(prompt)

    print("\n\nSample Local LLM with Open ai format usage..\n\n")
    print(f"Prompt : {prompt} ")
    print(result_json["choices"][0]["message"]["content"])
