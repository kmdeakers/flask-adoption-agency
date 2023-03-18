"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Database models and methods for Users"""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    pet_name = db.Column(
        db.String(50),
        nullable=False
    )

    species = db.Column(
        db.String(50),
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        nullable=False
    )

    age = db.Column(
        db.String(10),
        nullable=False
    )

    pet_notes = db.Column(
        db.Text,
        nullable=False
    )

    available = db.Column(
        db.Boolean,
        default=True
    )

    # @classmethod
    # def add_pet(cls, pet):
    #     """Takes in pet data and adds to database"""


    #     db.session.add(pet)
    #     db.session.commit()