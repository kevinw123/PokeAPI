from flask import Flask, jsonify, request
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/pokemon/api/v1.0/all/', methods=['GET'])
def get_all_pokemon():
    data = json.load(open('PokemonData.json'))
    pprint(data[0])
    return jsonify(data)

@app.route('/pokemon/api/v1.0/single/', methods=['GET'])
def get_one_pokemon():
    number = request.args.get('number', type = int)
    data = json.load(open('PokemonData.json'))
    pprint(data[number])
    return jsonify(data[number])

if __name__ == '__main__':
    app.run(debug=True)
