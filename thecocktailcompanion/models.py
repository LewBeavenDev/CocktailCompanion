from thecocktailcompanion import db
from sqlalchemy import String

class Drink(db.Model):
    # schema for the Drinks model
    id = db.Column(db.Integer, primary_key=True)
    drink_image = db.Column(db.String(255), nullable=True) 
    drink_name = db.Column(db.String(255), unique=True, nullable=False)
    drink_glass = db.Column(db.String(255), nullable=False)
    drink_ice = db.Column(db.String(255), nullable=False)
    drink_method = db.Column(db.String(255), nullable=False)
    drink_ingredients = db.Column(db.Text, nullable=False)
    drink_garnish = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return self.drink_name, self.drink_glass, self.drink_ice, self.drink_method, self.drink_ingredients, self.drink_garnish

    
    
