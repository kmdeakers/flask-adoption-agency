"""Flask app for adopt app."""

import os

from flask import Flask,redirect, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import FlaskForm
from wtforms import Stringfield, FloatField

from models import connect_db

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)
