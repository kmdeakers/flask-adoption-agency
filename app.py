"""Flask app for adopt app."""

import os

from flask import Flask,redirect, request, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

from models import connect_db, db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def show_pet_listing():
    """
    shows all pets
    """
    #get listing of all pets from database
    pets = Pet.query.all() #[obj, obj]
    #render html passing in pets
    return render_template("pet-listing.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet form; handle adding. """

    form = AddPetForm()

    if form.validate_on_submit():
        pet_name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        pet_notes = form.pet_notes.data

        pet = Pet(pet_name=pet_name, species=species, photo_url=photo_url,
                    age=age, pet_notes=pet_notes)
        # breakpoint()
        db.session.add(pet)
        db.session.commit()

        flash(f"{pet_name} added!")
        return redirect("/")

    else:
        return render_template('add-pet-form.html', form=form)

