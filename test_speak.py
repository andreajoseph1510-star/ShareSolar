import requests

resp = requests.post(
    "http://127.0.0.1:8000/voice/speak",
    params={"text": "Hello Ann, ShareSolar is ready!", "language": "en"}
)

with open("sample.mp3", "wb") as f:
    f.write(resp.content)
