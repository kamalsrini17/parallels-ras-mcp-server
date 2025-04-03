import os
from dotenv import load_dotenv

load_dotenv()

RAS_API_URL = os.getenv("RAS_API_URL")
RAS_USERNAME = os.getenv("RAS_USERNAME")
RAS_PASSWORD = os.getenv("RAS_PASSWORD")
