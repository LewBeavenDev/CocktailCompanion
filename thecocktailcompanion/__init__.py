from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Set up configurations
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default_secret_key")

    # Upload folder configuration (for file uploads)
    app.config['UPLOAD_FOLDER'] = 'thecocktailcompanion/static/uploads'

    # Check if in development or production mode
    if os.environ.get("DEVELOPMENT") == "True":
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # Dev DB URL
    else:
        # Get the database URL from the environment
        uri = os.environ.get("DATABASE_URL", "")  # Default to an empty string if not set
        if uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)
        app.config["SQLALCHEMY_DATABASE_URI"] = uri

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # User loader for Flask-Login
    from .models import User, Drink  # Ensure models are imported

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from . import routes
    app.register_blueprint(routes.main)

    return app
