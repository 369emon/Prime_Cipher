from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages = []

@app.route('-s', methods=['POST'])
def send_message():
    data = request.get_json()
    msg = data.get('message')
    sender = data.get('sender')
    if msg and sender:
        messages.append({'sender': sender, 'message': msg})
        return jsonify({"status": "Message received"}), 200
    return jsonify({"error": "Missing sender or message"}), 400

@app.route('/messages', methods=['GET'])
def get_messages():
    global messages
    msgs = messages[:]
    messages = []
    return jsonify({"messages": msgs})

@app.route('/')
def index():
    return "PrimeCipher Chat Server is running! Use /messages to get messages."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)