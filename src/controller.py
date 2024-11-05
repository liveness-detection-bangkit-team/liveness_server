from service import RegisterModel, LoginModel
from flask import jsonify


def register_controller(db, request_json):
    name = request_json.get("name")
    username = request_json.get("username")
    password = request_json.get("password")

    user = RegisterModel(name, username, password)

    valid, error_message = user.validate()
    if not valid:
        return jsonify({"status_code": 400, "message": error_message}), 400

    # check username exist
    username_exist, error_message = user.check_username(db)
    if username_exist:
        return jsonify({"status_code": 400, "message": error_message}), 400

    # hash password
    hash_password = user.hash_password()

    # insert user data to database
    success_message = user.insert_account(db, hash_password)

    # response success
    response_message = {"status_code": 201, "message": success_message}
    return jsonify(response_message), 201


def login_controller(db, request_json):
    username = request_json.get("username")
    password = request_json.get("password")

    login = LoginModel(username, password)

    valid, error_message = login.validate()
    if not valid:
        return jsonify({"status-code": 400, "message": error_message}), 400

    # check username exist

    # validate password
    # login_model.check_password(password)

    # response successs
    success_response = {"status_code": 200, "message": "Login successfully"}
    return jsonify(success_response), 200
