import requests
from flask import Flask, request

TOKEN = "8278972746:AAFkqNxjveag0xAYjAvp-IGALw7jk0--v00"
CHAT_ID = "5942003403"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    message = data.get("message", "No message")
    payload = {"chat_id": CHAT_ID, "text": message}
    r = requests.post(URL, json=payload)
    return r.json()

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
