from flask import Flask, render_template, request, redirect, url_for
import requests

# initial app configuration
app = Flask(__name__)

"""
A página inicial do aplicativo da web.
"""


@app.route('/')
def index():
    cars = [{"nome": "Fiat Mobi", "ano": 2021, "km": 0, "valor": 50000, "img_frente": "https://cdn.autopapo.com.br/box/uploads/2020/10/19101038/frente-do-fiat-mobi_trekking_2021-vermelho.jpeg", "img_traseira": "https://revistacarro.com.br/fiat-mobi-2021-ganha-versao-trekking-e-multimidia-da-strada/fiat-mobi-trekking-2021-2/"},
            {"nome": "Renault Sandero", "ano": 2019, "km": 1000, "valor": 35000,
                "img_frente": "https://quatrorodas.abril.com.br/wp-content/uploads/2016/11/5658c48552657372a12b0009658_sandero_01.jpeg?quality=70&strip=all", "img_traseira": ""},
            {"nome": "Ferrari Enzo", "ano": 2009, "km": 100, "valor": 700000,
                "img_frente": "https://upload.wikimedia.org/wikipedia/commons/8/8b/2003_Enzo_Ferrari_at_Greenwich_2018%2C_front_right.jpg", "img_traseira": ""},
            {"nome": "Ford Focus", "ano": 2018, "km": 10000, "valor": 28000, "img_frente": "https://quatrorodas.abril.com.br/wp-content/uploads/2018/04/ford_2018_focus_st-line__01.jpg?resize=1536,1025", "img_traseira": "https://quatrorodas.abril.com.br/wp-content/uploads/2018/04/ford_2018_focus_st-line__02.jpg?resize=1536,1023"}]

    return render_template('index.html', results=cars, title="carros")


@app.route('/<path:dummy>')
def fallback(dummy=None):
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html')
