from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from thecocktailcompanion import db
from thecocktailcompanion.models import User, Drink
from thecocktailcompanion.forms import RegistrationForm, LoginForm
from werkzeug.utils import secure_filename
import os

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/drinks')
def drinks():
    drinks = Drink.query.order_by(Drink.drink_name).all()
    return render_template('drinks.html', drinks=drinks)

@main.route('/register', methods=['GET', 'POST'])
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

@main.route('/login', methods=['GET', 'POST'])
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

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    drinks = Drink.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', drinks=drinks)

@main.route('/edit/<int:drink_id>', methods=['GET', 'POST'])
@login_required
def edit_drink(drink_id):
    drink = Drink.query.get_or_404(drink_id)
    if drink.user_id != current_user.id:
        flash('You do not have permission to edit this drink', 'danger')
        return redirect(url_for('main.dashboard'))
    if request.method == "POST":
        drink.drink_name = request.form.get("drink_name")
        db.session.commit()
        return redirect(url_for("main.drinks"))
    return render_template('edit_drink.html', drink=drink)

@main.route('/delete/<int:drink_id>', methods=['POST'])
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

@main.route('/add_drink', methods=["GET", "POST"])
@login_required
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

            relative_file_path = filename
            new_drink = Drink(
                drink_name=drink_name,
                drink_glass=drink_glass,
                drink_ice=drink_ice,
                drink_method=drink_method,
                drink_ingredients=drink_ingredients,
                drink_garnish=drink_garnish,
                drink_image=relative_file_path,
                user_id=current_user.id
            )
            db.session.add(new_drink)
            db.session.commit()
            return redirect(url_for('main.drinks'))

    return render_template('add_drink.html')
