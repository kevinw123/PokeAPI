from flask import Flask, jsonify
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    data = json.load(open('data.json'))
    pprint(data)
    return jsonify(data)

@app.before_first_request
def startup():
    print("First Run")

if __name__ == '__main__':
    app.run(debug=True)