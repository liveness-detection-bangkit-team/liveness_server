import jwt
from variable import JWT_KEY, EXPIRES


# generate JWT token for 30 minutes
def generate_jwt(username):
    payload = {"user_id": username, "expired": EXPIRES.isoformat()}

    return jwt.encode(payload, JWT_KEY, algorithm="HS256")


# decode JWT token to get user_id
def decode_jwt(token):
    payload = jwt.decode(token, JWT_KEY, algorithms=["HS256"])
    user_id = payload["user_id"]

    return user_id
