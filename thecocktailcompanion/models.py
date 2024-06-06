from thecocktailcompanion import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drink_image = db.Column(db.String(255), nullable=True)
    drink_name = db.Column(db.String(255), unique=True, nullable=False)
    drink_glass = db.Column(db.String(255), nullable=False)
    drink_ice = db.Column(db.String(255), nullable=False)
    drink_method = db.Column(db.String(255), nullable=False)
    drink_ingredients = db.Column(db.Text, nullable=False)
    drink_garnish = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_global = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Drink {self.drink_name}>"
