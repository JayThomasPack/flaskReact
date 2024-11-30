# backend/app/config.py
DATABASE_URI = ''
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

class Config:
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
    DB_NAME = "questionnaire_db"
    DB_USER = "postgres"
    DB_PASSWORD = os.getenv("DB_PASSWORD", "your_default_password")
    DB_HOST = "localhost"
