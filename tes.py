import requests
url = "http://127.0.0.1:8000"
b = {
  "id": 18220079,
  "name": "Zafran Divac A"
}
a = requests.get(url, json=b)

print(a.text)