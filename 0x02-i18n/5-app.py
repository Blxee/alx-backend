#!/usr/bin/env python3
"""5. Mock logging in"""
from typing import Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Config object for babel."""
    LAGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id: int) -> Union[dict, None]:
    return users.get(id)


@app.before_request
def before_request() -> None:
    id = request.args.get('login_as')
    try:
        if id is not None:
            id = int(id)
            g.user = get_user(id)
    except Exception:
        pass


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
    return render_template('5-index.html')
