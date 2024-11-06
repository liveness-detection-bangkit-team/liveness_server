from flask import Flask
from dotenv import load_dotenv
from database import init_db, db
import os
from routes import bp

load_dotenv()


def init_app():
    flask_app = Flask(__name__)

    database_url = os.getenv("DATABASE_URL")

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    init_db(flask_app)
    flask_app.register_blueprint(bp)

    return flask_app


app = init_app()


# create table
with app.app_context():
    db.create_all()

if __name__ == "__name__":
    app.run(host="0.0.0.0", port=5000, debug=True)
