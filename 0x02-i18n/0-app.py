#!/usr/bin/env python3
"""0. Basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('templates/0-index.html')
