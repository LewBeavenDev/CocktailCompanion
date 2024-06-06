from thecocktailcompanion import create_app, db
from thecocktailcompanion.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Ensure the database is created
    db.create_all()

    # Check if admin user exists
    admin_user = User.query.filter_by(username="admin").first()
    if not admin_user:
        # Create admin user if it doesn't exist
        admin_user = User(
            username="admin",
            password=generate_password_hash("password", method='pbkdf2:sha256'),
            is_admin=True
        )
        db.session.add(admin_user)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
