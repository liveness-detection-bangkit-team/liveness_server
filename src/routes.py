from controller import login_controller, register_controller, logout_controller
from flask import jsonify, request, Blueprint
from helper import decode_jwt

bp = Blueprint("main", __name__)


@bp.route("/auth/register", methods=["POST"])
def register():
    request_json = request.get_json()
    return register_controller(request_json)


@bp.route("/auth/login", methods=["POST"])
def login():
    request_json = request.get_json()
    return login_controller(request_json)


@bp.route("/auth/logout", methods=["DELETE"])
def logout():
    return logout_controller()


@bp.route("/", methods=["GET"])
def main():
    token = request.cookies.get("X-LIVENESS-TOKEN")
    if token:
        user_id = decode_jwt(token)
        return jsonify({"message": f"Your user_id: {user_id}"})

    response = {"status_code": 200, "message": "You found me!"}
    return jsonify(response), 200
