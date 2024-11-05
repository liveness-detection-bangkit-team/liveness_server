import bcrypt
from sqlalchemy import text


class RegisterModel:
    MIN_INPUT_LENGTH = 5

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def validate(self):
        errors = {}

        if not self.name or not self.username or not self.password:
            errors["error"] = "Name, Username, and Password is required"

        if errors:
            return False, errors

        if (
            len(self.username) < self.MIN_INPUT_LENGTH
            or len(self.password) < self.MIN_INPUT_LENGTH
            or len(self.name) < self.MIN_INPUT_LENGTH
        ):
            errors["error"] = (
                f"Name, Username, and Password at least {self.MIN_INPUT_LENGTH} characters"
            )

        isValid = len(errors) == 0
        return isValid, errors

    def check_username(self, db):
        sql = text("SELECT username FROM users WHERE username = :username LIMIT 1")
        result = db.session.execute(sql, {"username": self.username})

        user = result.fetchone()  # Fetch the first (and only) result

        # Check if user exists
        is_exist = user is not None
        errorMessage = "Username already exists!" if is_exist else ""

        return is_exist, errorMessage

    def hash_password(self):
        password_bytes = self.password.encode("utf-8")
        hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed_bytes

    def insert_account(self, db, hash_password):
        sql = text(
            "INSERT INTO users (name, username, password) VALUES (:name, :username, :password)"
        )
        db.session.execute(
            sql,
            {"name": self.name, "username": self.username, "password": hash_password},
        )
        db.session.commit()

        return "Register successfully!"


class LoginModel:
    MIN_INPUT_LENGTH = 5

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate(self):
        errors = {}

        if not self.username or not self.password:
            errors["error"] = "Username and Password is required"

        if errors:
            return False, errors

        if (
            len(self.username) < self.MIN_INPUT_LENGTH
            or len(self.password) < self.MIN_INPUT_LENGTH
        ):
            errors["error"] = (
                f"Username or Password at least {self.MIN_INPUT_LENGTH} characters"
            )

        isValid = len(errors) == 0
        return isValid, errors

    def check_password(self, password):
        if bcrypt.checkpw(b"", password):
            print("match")
        else:
            print("doesn't match")
