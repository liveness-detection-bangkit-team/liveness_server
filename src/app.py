from flask import Flask
from database import init_db, db
from routes import bp
from variable import DATABASE_URL
from flask_cors import CORS


def init_app():
    flask_app = Flask(__name__)

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    init_db(flask_app)

    # register routes
    flask_app.register_blueprint(bp)

    return flask_app


app = init_app()
CORS(
    app,
    resources={
        r"/*": {
            "origins": ["*"],
            "methods": ["GET", "POST", "DELETE", "PUT"],
        },
    },
    supports_credentials=True,
)

# create table
with app.app_context():
    db.create_all()

if __name__ == "__name__":
    app.run(host="0.0.0.0", port=5000, debug=True)
