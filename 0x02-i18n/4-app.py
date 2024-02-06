#!/usr/bin/env python3
"""4. Force locale with URL parameter"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config object for babel."""
    LAGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the best locale match for user preference."""
    lang = request.args.get('locale')
    if lang in Config.LAGUAGES:
        return lang
    return (request.accept_languages.best_match(Config.LAGUAGES)
            or Config.BABEL_DEFAULT_LOCALE)


@app.route('/')
def index() -> str:
    """Function to handle the main / route."""
    return render_template('4-index.html')
