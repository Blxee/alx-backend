#!/usr/bin/env python3
"""1. Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
app.config['LAGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def index() -> str:
    """Function to handle the main / route."""
    return render_template('1-index.html')
