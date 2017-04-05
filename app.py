import json

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/ping', methods=['GET', 'PUT'])
def manage_data():
    data = []
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

    if request.method == 'PUT':
        request_data = json.loads(request.data)
        data = request_data

        with open('data.json', 'w') as json_file:
            data_to_write = json.dumps(data, indent=4)
            json_file.write(data_to_write)

        return jsonify(data)
    else:
        return jsonify(data)
    