from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = environ.get(
        'DATABASE_URL', 'sqlite:///employee.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get('SECRET_KEY', 'your-secret-key-here')
