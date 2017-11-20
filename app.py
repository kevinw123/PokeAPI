from flask import Flask, jsonify
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/pokemon/api/v1.0/all/', methods=['GET'])
def get_all_pokemon():
    data = json.load(open('PokemonData.json'))
    pprint(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
