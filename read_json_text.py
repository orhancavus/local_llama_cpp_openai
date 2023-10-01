import json

file_name = "api_result.json"

with open(file_name, "r") as fn:
    llama_result = fn.read()

    llama_json = json.loads(llama_result)

    content = llama_json.get("content", "")

    print(content)
