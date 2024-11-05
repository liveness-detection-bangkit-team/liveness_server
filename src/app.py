from flask import Flask
from dotenv import load_dotenv
from database import init_db, db
import os
from datetime import datetime
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


# Initial table for users
class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def __repr__(self):
        return f"<User('{self.name}')>"


with app.app_context():
    db.create_all()

if __name__ == "__name__":
    app.run(host="0.0.0.0", port=5000, debug=True)
