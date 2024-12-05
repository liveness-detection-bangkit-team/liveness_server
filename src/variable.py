import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
JWT_KEY = os.getenv("JWT_KEY")
EXPIRES = datetime.now() + timedelta(minutes=60)
MAX_AGE_TOKEN = 60 * 60
