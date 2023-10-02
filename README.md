# Run local LLM as OPENAI API through llama.cpp

For more details how to install llama.cpp : https://github.com/ggerganov/llama.cpp

```text
Orhan Cavus
02.10.2023
```

## OPENAI api format

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


### 2. Start Local LLM server llama.cpp folder

```bash
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

### 4. Call from Terminal

```bash
# call from terminal
curl http://127.0.0.1:8081/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }' 

```
