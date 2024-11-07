from service import RegisterModel, Loginmodel
from flask import jsonify
from repository import check_username, insert_account


def register_controller(request_json):
    name = request_json.get("name")
    username = request_json.get("username")
    password = request_json.get("password")

    user = RegisterModel(name, username, password)

    valid, error_message = user.validate()
    if not valid:
        return jsonify({"status_code": 400, "message": error_message["error"]}), 400

    # check username exist
    username_exist = check_username(username)
    if username_exist:
        return jsonify({"status_code": 400, "message": "Username already exist!"}), 400

    # hash password
    hash_password = user.hash_password()

    # insert user data to database
    success_message = insert_account(name, username, hash_password)

    # response success
    response_message = {"status_code": 201, "message": success_message}
    return jsonify(response_message), 201


def login_controller(request_json):
    username = request_json.get("username")
    password = request_json.get("password")

    login = Loginmodel(username, password)

    valid, error_message = login.validate()
    if not valid:
        return jsonify({"status-code": 400, "message": error_message["error"]}), 400

    # check username exist
    username_exist = check_username(username)
    if not username_exist:
        return jsonify(
            {"status_code": 400, "message": "Username or Password is wrong!"}
        ), 400

    # verify password
    valid = login.check_password(password)
    if not valid:
        return jsonify(
            {"status_code": 400, "message": "Username or password is wrong!"}
        ), 400

    # response successs
    success_response = {"status_code": 200, "message": "Login successfully!"}
    return jsonify(success_response), 200
