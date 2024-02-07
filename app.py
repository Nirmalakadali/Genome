import json
from flask import Flask, request, jsonify
import requests
import os
app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/add_condition', methods=['POST'])
def add_condition():
    request_data = request.json
    json_url = request_data.get('https://drive.google.com/file/d/1fSy-Fd248OZzY-80v5uqrol3wfWlUxNB/view?usp=sharing')
    
    if not json_url:
        return jsonify({"error": "JSON URL not provided"}), 400

    # Fetch JSON data from the provided URL
    try:
        response = requests.get(json_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        new_condition = response.json()
    except Exception as e:
        return jsonify({"error": f"Failed to fetch JSON data: {str(e)}"}), 500

    # Path to the local config file
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')

    # Read existing data from the local config file
    with open(json_url, 'r') as file:
        data = json.load(file)

    # Append new condition to the existing data
    data['conditions'].append(new_condition)

    # Write updated data back to the local config file
    with open(json_url, 'w') as file:
        json.dump(data, file, indent=4)

    return jsonify({"message": "Condition added successfully"})

if __name__ == '__main__':
    app.run(debug=True)
