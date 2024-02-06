#!/usr/bin/env python3
"""0. Basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Function to handle the main / route."""
    return render_template('0-index.html')
