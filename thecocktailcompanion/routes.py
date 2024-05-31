import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from thecocktailcompanion import app, db
from thecocktailcompanion.models import Drink

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


@app.route('/edit_drink/<int:drink_id>', methods=["GET", "POST"])
def edit_drink(drink_id):
    drink = Drink.query.get_or_404(drink_id)
    if request.method == "POST":
        drink.drink_name = request.form.get("drink_name")
        db.session.commit()
        return redirect(url_for("drinks"))    
    return render_template("edit_drink.html", drink=drink)
    
    
@app.route('/delete_drink/<int:drink_id>')
def delete_drink(drink_id):
    drink = Drink.query.get_or_404(drink_id) 
    db.session.delete(drink)
    db.session.commit()
    return redirect(url_for("drinks"))