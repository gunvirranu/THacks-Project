from flask import Flask, jsonify
from flask import abort, make_response, request
# import models

app = Flask(__name__)

users = [{
        'id': 0,
        'user': 'gunvir',
        'pass': 'qwerty',
        'first': 'Gunvir',
        'email': 'g1ranu@gmail.com',
        'login_id': None,
        'max_donation': 0.50,
        'min_amount': 100.00,
        'period': 1,
        'month': 427.17
    }]

def get_new_id():
    return users[-1]['id'] + 1

@app.route('/api/users/all', methods=['GET'])
def get_all_users():
    return jsonify({'users': users})
    # return jsonify({'users': models.select_user()})

@app.route('/api/users/get/<string:username>', methods=['GET'])
def get_user(username):
    user = [user for user in users if user['user'] == username]
    # user = models.select_by_username(username)
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

@app.route('/api/users/create', methods=['POST'])
def add_user():
    if not request.json or not 'user' in request.json:
        abort(400)
    user = {
        'id': get_new_id(),
        'user': request.json['user'],
        'pass': request.json['pass'],
        'first': request.json['first'],
        'email': request.json['email'],
        'max_donation': 0.50,
        'min_amount': 25.00,
        'period': 2,
        'month': 0,
        'login_id': None
    }
    users.append(user)

    # models.insert_user(user['user'], user['email'], user['pass'], user['first'])

    return jsonify({'user': user}), 201

@app.route('/api/users/update/<string:username>', methods=['PUT'])
def update_user(username):
    user = [user for user in users if user['user'] == username]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    for n in ['max_donation', 'min_amount', 'month']:
        if n in request.json and type(request.json[s]) is not float:
            abort(400)
    if 'period' in request.json and type(request.json['period']) is not int:
        abort(400)
    for i in ['user', 'pass', 'first', 'email', 'max_donation', 'min_amount', 'period', 'month']:
        user[0][i] = request.json.get(i, user[0][i])
    return jsonify({'user': user[0]}) 

@app.route('/api/users/remove/<string:username>', methods=['DELETE'])
def delete_user(username):
    user = [user for user in users if user['user'] == username]
    if len(user) == 0:
        abort(404)
    users.remove(users[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
