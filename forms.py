"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField

class AddPetForm(FlaskForm):
    """Form for adding pets. """

    pet_name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    pet_notes = StringField("Notes")
