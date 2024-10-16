from thecocktailcompanion import create_app, db
from thecocktailcompanion.models import User
from werkzeug.security import generate_password_hash
import os

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable or default to 5000
    app.run(host="0.0.0.0", port=port)