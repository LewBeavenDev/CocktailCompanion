from flask import Flask, render_template, request, redirect, url_for
from thecocktailcompanion import app, db
from thecocktailcompanion.models import Drinks

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/library")
def library():
    return render_template("library.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")
