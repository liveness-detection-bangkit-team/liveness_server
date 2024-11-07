from sqlalchemy import text
from database import db


def check_username(username):
    sql = text("SELECT username FROM users WHERE username = :username LIMIT 1")
    result = db.session.execute(sql, {"username": username})

    user = result.fetchone()

    is_exist = user is not None

    return is_exist


def insert_account(name, username, hash_password):
    sql = text(
        "insert into users (name, username, password) values (:name, :username, :password)"
    )
    db.session.execute(
        sql,
        {"name": name, "username": username, "password": hash_password},
    )
    db.session.commit()

    return "Successfully created account!"


def get_hashed_password(username):
    sql = text("SELECT password FROM users WHERE username = :username LIMIT 1")
    result = db.session.execute(sql, {"username": username})

    row = result.fetchone()

    return row[0] if row else None
