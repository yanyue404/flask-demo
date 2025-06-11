from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# 配置
app.config.from_object('config.DevelopmentConfig')

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/api/status")
def status():
    return jsonify({"status": "ok"})

@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
