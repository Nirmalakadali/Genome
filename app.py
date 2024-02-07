import json
from flask import send_from_directory,Flask, request, jsonify
import os 
app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/add_condition', methods=['POST'])

def add_condition():
    new_condition = request.json
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')

    with open(config_path, 'r') as file:
        data = json.load(file)

    data['conditions'].append(new_condition)

    with open(config_path, 'w') as file:
        json.dump(data, file, indent=4)

    return jsonify({"message": "Condition added successfully"})

if __name__ == '__main__':
    app.run(debug=True)
