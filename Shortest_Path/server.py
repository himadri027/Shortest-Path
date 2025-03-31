from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Shortest Path API!"

@app.route('/run')
def run_visualization():
    subprocess.Popen(["python3", "runner.py"])
    return jsonify({"message": "Visualization started!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
