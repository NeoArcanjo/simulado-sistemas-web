from typing import Collection
from flask import Flask, render_template, request
import requests

# initial app configuration
app = Flask(__name__)

"""
A página inicial do aplicativo da web.
"""
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/<page>', methods=['GET'])
def page(page):
    offset = request.args.get('offset')
    print(offset)
    limit = request.args.get('limit')

    url = f"https://pokeapi.co/api/v2/{page}?offset={offset}&limit={limit}"

    # search = request.args.get('q')
    # results = requests.get(f"{url}{search}")
    
    results = requests.get(url)
    results = results.json()
    if page == "pokemon":
        collection = []
        for result in results['results']:
            r = requests.get(result['url'])
            collection.append(r.json())
        results = collection
    
    return render_template('%s.html' % page, results=results)

# url = "https://pokeapi.co/api/v2/pokemon?offset=" + this.state.offset + "&limit=" + this.state.loadNumber
@app.route('/<page>/search', methods=['GET'])
def search(page):
    url = f"https://pokeapi.co/api/v2/{page}/"

    search = request.args.get('q')
    results = requests.get(url + search)
    print(results.json())
    return results.json()


@app.route('/<page>/<name>/detail', methods=['GET'])
def about(page, name):
    url = f"https://pokeapi.co/api/v2/{page}/{name}"

    results = requests.get(url)
    return render_template('about-%s.html' % page, result=results.json())




