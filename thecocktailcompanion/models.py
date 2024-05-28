from thecocktailcompanion import db


class Drinks(db.Model):
    # schema for the Drinks model
    id = db.Column(db.integer, primary_key=True)
    drink_name = db.Column(db.String(25), unique=True, nullable=False)
    drink_glass = db.Column(db.String(25), nullable=False)
    drink_ice = db.Column(db.String(10), nullable=False)
    drink_method = db.Column(db.String(100), nullable=False)
    drink_ingredients = db.Column(db.Text, nullable=False)
    drink_garnish = db.Column(db.String(25), nullable=True)
