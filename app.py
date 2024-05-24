import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/library")
def library():
    return render_template("library.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True,
    )
