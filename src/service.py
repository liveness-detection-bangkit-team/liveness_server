import bcrypt
from repository import get_hashed_password


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

    def hash_password(self):
        password_bytes = self.password.encode("utf-8")
        hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed_bytes


class Loginmodel:
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
        bytes_pass = password.encode("utf-8")

        hash_password = get_hashed_password(self.username)
        bytes_hash_pass = hash_password.encode("utf-8")

        if bcrypt.checkpw(bytes_pass, bytes_hash_pass):
            return True
        return False
