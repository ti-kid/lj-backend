from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow all origins

@app.route("/")
def home():
    return jsonify({"message": "Hello from Python backend!"})

