#!/usr/bin/env python3
"""1. Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LAGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """Function to handle the main / route."""
    return render_template('1-index.html')
