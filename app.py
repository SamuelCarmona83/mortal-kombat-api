from flask import Flask, jsonify, request, abort

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


def reqVal(request_body, keys):
    values = []
    for key in keys:
        if key not in request_body:
            abort(400, description=f"Missing required field: {key}")
        value = request_body.get(key)
        values.append(value)
    return tuple(values)


@api.route('/characters', methods=['POST'])
def add_character():

    body = request.get_json()
    name, height, weight, style = reqVal(
        body, ['name', 'height', 'weight', 'fighting_style']
    )
    new_character = MortalKombatCharacter(name, height, weight, style)
    return jsonify(new_character.serialize()), 201

# El metodo Delete no recive body, por lo que solo se necesita el nombre en la URL
@api.route('/characters/<string:name>', methods=['DELETE'])
def delete_character(name):

    character = MortalKombatCharacter.find_by_name(name)

    if not character:
        abort(404, description="Character not found")

    MortalKombatCharacter.remove_character(character)

    return jsonify({"message": f"Character {name} deleted"}), 200

if __name__ == '__main__':
    api.run(debug=True)
