from database import db
from controller import login_controller, register_controller
from flask import jsonify, request, Blueprint

bp = Blueprint("main", __name__)


@bp.route("/auth/register", methods=["POST"])
def register():
    request_json = request.get_json()
    return register_controller(db, request_json)


@bp.route("/auth/login", methods=["POST"])
def login():
    request_json = request.get_json()
    return login_controller(db, request_json)


@bp.route("/", methods=["GET"])
def main():
    response = {"status_code": 200, "message": "You found me!"}
    return jsonify(response), 200
