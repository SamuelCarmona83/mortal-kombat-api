from flask import Flask, jsonify

from models import MortalKombatCharacter

api = Flask(__name__)


@api.route('/')
def home():
    return jsonify({"message": "Welcome to the API"}), 200

@api.route('/characters')
def get_characters():
    return jsonify(
        [ item.serialize() for item in MortalKombatCharacter.get_all() ]
    ), 200

if __name__ == '__main__':
    api.run(debug=True)
