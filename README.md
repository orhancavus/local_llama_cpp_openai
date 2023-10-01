# llama.cpp as web server consumer apps

## Usage from terminal

curl --request POST \\n    --url http://localhost:8080/completion \\n    --header "Content-Type: application/json" \\n    --data '{"prompt": "Building a website can be done in 10 simple steps:","n_predict": 128}' > api_result.json

## Result from terminal

cat api_result.json | python -m json.tool
