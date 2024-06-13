from thecocktailcompanion import create_app, db
from thecocktailcompanion.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    admin_user = User.query.filter_by(username="admin").first()
    if not admin_user:
        admin_user = User(
            username="admin",
            password=generate_password_hash("password", method='pbkdf2:sha256'),
            is_admin=True
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")
