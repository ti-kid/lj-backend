from flask import Flask, jsonify
from flash_cors import CORS

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Python backend!"})
    CORS(app, origins=["https://yellowantjeff.github.io"])

