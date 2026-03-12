import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "5"))