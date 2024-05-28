from thecocktailcompanion import routes
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default_secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DB_URL", "sqlite:///default.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print("DB_URL:", app.config["SQLALCHEMY_DATABASE_URI"])
print("SECRET_KEY:", app.config["SECRET_KEY"])

db = SQLAlchemy(app)
