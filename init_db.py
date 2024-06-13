from thecocktailcompanion import create_app, db
from thecocktailcompanion.models import User, Drink

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created.")
