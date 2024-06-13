import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fe79d3f6e6dac0f7b94289aae8bfebcdd8f65ba102db43cc93f1ec55a6fed4c3'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@localhost/thecocktailcompanion'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'thecocktailcompanion', 'static', 'uploads')


