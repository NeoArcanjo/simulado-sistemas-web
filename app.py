from flask import Flask, render_template, request, redirect, url_for
import requests

# initial app configuration
app = Flask(__name__)

"""
A página inicial do aplicativo da web.
"""


@app.route('/')
def index():
    cars = [{"name": "Fiat Mobi", "ano": 2021, "km": 0, "valor": 50000}, {"name": "Renault Sandero", "ano": 2019, "km": 1000, "valor": 35000},
            {"name": "Ferrari Enzo", "ano": 2009, "km": 100, "valor": 700000}, {"name": "Ford Focus", "ano": 2018, "km": 10000, "valor": 28000}]

    return render_template('index.html', results=cars, title="carros")


@app.route('/<path:dummy>')
def fallback(dummy=None):
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html')
