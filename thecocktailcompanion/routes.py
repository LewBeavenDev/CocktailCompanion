from flask import Flask, render_template, url_for, redirect, request
from thecocktailcompanion import app, db
from thecocktailcompanion.models import Drink


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/library')
def library():
    return render_template('library.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/add_drink', methods=["GET", "POST"])
def add_drink():
    if request.method == "POST":
        drink = Drink(
            drink_name=request.form.get("drink_name"),
            drink_glass=request.form.get("drink_glass"),
            drink_ice=request.form.get("drink_ice"),
            drink_method=request.form.get("drink_method"),
            drink_ingredients=request.form.get("drink_ingredients"),
            drink_garnish=request.form.get("drink_garnish"),
            )
        db.session.add(drink)
        db.session.commit()
        return redirect(url_for("library"))
    return render_template('add_drink.html')