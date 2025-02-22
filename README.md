# Run local LLM as OPENAI API through llama.cpp

This Python script showcases how to interact with OpenAI's GPT-3.5 Turbo model compatible Local LLM running with llama.cpp to generate text completions. It sends a user-provided prompt to a locally hosted instance of the model and retrieves the generated text. This readme explains how to use the script and provides some context.

For more details how to install llama.cpp : <https://github.com/ggerganov/llama.cpp>

```text
Application : local_llama_cpp_openai
Author      : Orhan Cavus
Created     : 02.10.2023
```

## Call with OPENAI api format

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'
```

### 1. Start local LLM and API server separetely

### 2. Start Local LLM server from the llama.cpp folder with appropriate model

```bash
# Start local llama.cpp from llama.cpp main folder
./server -c 4096 --host 0.0.0.0 -t 16 --mlock -m ./models/codellama-13b-instruct.Q4_K_M.gguf
```

### 3. Start Local API server

```bash
# Activate enviroment and Start API server
 %  source venv/bin/activate

 venv  %  python api_like_OAI.py
 * Serving Flask app 'api_like_OAI'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8081
Press CTRL+C to quit
```

### 4. Test Call LLM engine from terminal with curl

```bash
# Call the service
curl --request POST \
    --url http://localhost:8080/completion \
    --header "Content-Type: application/json" \
    --data '{"prompt": "Building a website can be done in 10 simple steps:","n_predict": 128}' | jq '.content' | while IFS= read -r line; do echo -e "$line"; done
```

### 5. Test Call API from terminal with curl

```bash
# Call the service
curl http://127.0.0.1:8081/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }' 
```

or with llama_api_client.py

```bash
python llama_api_client.py "Explain prime numbers"
```

### 6. Test modules

You can run the tests using the following command from the root of your project:

```bash
pytest test/
```
