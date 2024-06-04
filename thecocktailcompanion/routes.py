import os
from flask import Flask, render_template, request, redirect, url_for, blueprint, flash
from werkzeug.utils import secure_filename
from thecocktailcompanion import app, db
from thecocktailcompanion.models import Drink
from models import db, User, Drink
from thecocktailcompanion.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


@main_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main_blueprint.route('/dashboard')
@login_required
def dashboard():
    drinks = Drink.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', drinks=drinks)


@main_blueprint.route('/edit/<int:drink_id>', methods=['GET', 'POST'])
@login_required
def edit_drink(drink_id):
    drink = Drink.query.get_or_404(drink_id)
    if drink.user_id != current_user.id:
        flash('You do not have permission to edit this drink', 'danger')
        return redirect(url_for('main.dashboard'))
    if request.method == "POST":
        drink.drink_name = request.form.get("drink_name")
        db.session.commit()
        return redirect(url_for("drinks")) 
    # ...
    return render_template('edit_drink.html', drink=drink)

@main_blueprint.route('/delete/<int:drink_id>', methods=['POST'])
@login_required
def delete_drink(drink_id):
    drink = Drink.query.get_or_404(drink_id)
    if drink.user_id != current_user.id:
        flash('You do not have permission to delete this drink', 'danger')
        return redirect(url_for('main.dashboard'))
    db.session.delete(drink)
    db.session.commit()
    flash('Drink has been deleted', 'success')
    return redirect(url_for('main.dashboard'))
    

UPLOAD_FOLDER = 'thecocktailcompanion/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/drinks')
def drinks():
    drinks = list(Drink.query.order_by(Drink.drink_name).all())
    return render_template('drinks.html', drinks=drinks)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/add_drink', methods=["GET", "POST"])
def add_drink():
    if request.method == 'POST':
        drink_name = request.form.get('drink_name')
        drink_glass = request.form.get('drink_glass')
        drink_ice = request.form.get('drink_ice')
        drink_method = request.form.get('drink_method')
        drink_ingredients = request.form.get('drink_ingredients')
        drink_garnish = request.form.get('drink_garnish')

        file = request.files['drink_image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Store only the filename in the database
            relative_file_path = filename  # Only store the filename
            
            new_drink = Drink(
                drink_name=drink_name,
                drink_glass=drink_glass,
                drink_ice=drink_ice,
                drink_method=drink_method,
                drink_ingredients=drink_ingredients,
                drink_garnish=drink_garnish,
                drink_image=relative_file_path  # Store only the filename
            )
            db.session.add(new_drink)
            db.session.commit()
            return redirect(url_for('drinks'))

    return render_template('add_drink.html')




