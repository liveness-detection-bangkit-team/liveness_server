import os
from dotenv import load_dotenv
import datetime

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
JWT_KEY = os.getenv("JWT_KEY")
EXPIRES = datetime.datetime.now() + datetime.timedelta(minutes=30)