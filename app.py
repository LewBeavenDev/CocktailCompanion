from thecocktailcompanion import app, db
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
import os
from thecocktailcompanion import routes  # Import routes for blueprint

app = Flask(__name__)
secret_key = os.urandom(24)
print(secret_key)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register the blueprint after defining app and login manager
app.register_blueprint(routes.main_blueprint)

if __name__ == "__main__":
    app.run(
        debug=True
    )
