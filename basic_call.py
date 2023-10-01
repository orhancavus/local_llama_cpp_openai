import requests as r

url = "https://www.google.com"

call_text = r.get(url)

print(call_text.text)
