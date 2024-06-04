import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/thecocktailcompanion'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
