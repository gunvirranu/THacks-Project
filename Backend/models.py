import sqlite3 as sql


def create_db(name):
    try:
        with sql.connect('users.db') as con:
            pass
    except:
        pass


def insert_user(username, email, password, first):
    with sql.connect('users.db') as con:
        cur = con.cursor()
        cur.execute('INSERT INTO users (user, email, pass, first) VALUES (?,?,?,?)', (username, email, password, first))
        con.commit()


def select_user(params=()):
    with sql.connect('users.db') as con:
        cur = con.cursor()
        if params == ():
            result = cur.execute('SELECT * FROM users')

    return [format_dict(i) for i in result.fetchall()]


def select_by_username(username):
    with sql.connect('users.db') as con:
        cur = con.cursor()
        result = cur.execute("SELECT * FROM users WHERE user=?;", (username,)).fetchall()
    return format_dict(result[0])


# def update_user(username, user):
#     with sql.connect('users.db') as con:
#         cur = con.cursor()

#         updates=()
#         for key, val in user.items():
#             cur.execute("UPDATE users SET ?=? WHERE user=?;", (key, val, username))
#         cur.commit()


def format_dict(x):
    user = {}
    for i, a in enumerate(['id', 'user', 'email', 'pass', 'first', 'period', 'max_donation', 'min_amount']):
        user[a] = x[i]
    return user