import json

# Specify the path to your JSON file
json_file_path = "api_result.json"  # Replace with the actual file path

try:
    # Open the JSON file for reading
    with open(json_file_path, "r") as json_file:
        # Load the JSON data from the file
        data = json.load(json_file)

        # Extract the "content" field from the JSON data
        content = data.get("content", "")

        # Print the extracted content
        print(content)

except FileNotFoundError:
    print(f"File not found: {json_file_path}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {str(e)}")
