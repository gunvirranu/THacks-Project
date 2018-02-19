from flask import Flask, jsonify
from flask import abort, make_response, request
import models

app = Flask(__name__)

@app.route('/api/users/all', methods=['GET'])
def get_all_users():
    return jsonify({'users': models.select_user()})

@app.route('/api/users/<string:username>', methods=['GET'])
def get_user(username):
    user = models.select_by_username(username)
    if len(user) == 0:
        abort(404)
    return jsonify({'users': user})

@app.route('/api/users', methods=['POST'])
def add_user():
    if not request.json or not 'user' in request.json:
        abort(400)

    user = request.json['user']

    models.insert_user(user, request.json['email'], request.json['pass'], request.json['first'])

    return jsonify({'users': models.select_by_username(user)}), 201


# @app.route('/api/users/<string:username>', methods=['PUT'])
def update_user(username):
    user = models.select_by_username(username)
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    for n in ['max_donation', 'min_amount', 'month']:
        if n in request.json and type(request.json[s]) is not float:
            abort(400)
    if 'period' in request.json and type(request.json['period']) is not int:
        abort(400)

    for i in ['user', 'pass', 'first', 'email', 'max_donation', 'min_amount', 'period']:
        user[i] = request.json.get(i, user[i])

    models.update_user(username, user)
    return get_user(username)

# @app.route('/api/users/<string:username>', methods=['DELETE'])
# def delete_user(username):
#     user = [user for user in users if user['user'] == username]
#     if len(user) == 0:
#         abort(404)
#     users.remove(users[0])
#     return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':

    app.run(debug=True)
