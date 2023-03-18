"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Optional, URL



class AddPetForm(FlaskForm):
    """Form for adding pets. """

    pet_name = StringField("Pet Name")
    species = SelectField('Species', choices=[('dog', 'Dog'),
                                              ('cat', 'Cat'),
                                              ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(),URL()])
    age = SelectField("Age", choices=[('baby', 'Baby'),
                                              ('young', 'Young'),
                                              ('adult', 'Adult'), ('senior', 'Senior')])
    pet_notes = StringField("Notes")
