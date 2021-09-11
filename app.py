from flask import Flask, render_template, request, redirect, url_for
import requests

# initial app configuration
app = Flask(__name__)

pages = ["pokemon", "move", "type"]

"""
A página inicial do aplicativo da web.
"""
@app.route('/')
def index():
    return render_template('base.html')


@app.route('/<page>', methods=['GET'])
def page(page):
    if page not in pages:
        return redirect(url_for('index'))
    
    offset = request.args.get('offset')
    limit = request.args.get('limit')

    url = f"https://pokeapi.co/api/v2/{page}?offset={offset}&limit={limit}"

    results = requests.get(url)
    results = results.json()
    if 'results' in results.keys():
        collection = []
        for result in results['results']:
            r = requests.get(result['url'])
            collection.append(r.json())
        results = collection

    return render_template('%s.html' % page, results=results, title=page)

# url = "https://pokeapi.co/api/v2/pokemon?offset=" + this.state.offset + "&limit=" + this.state.loadNumber


@app.route('/<page>/search', methods=['GET'])
def search(page):
    if page not in pages:
        return redirect(url_for('index'))

    search = request.args.get('q')
    url = f"https://pokeapi.co/api/v2/{page}/{search}"

    results = requests.get(url)
    if results.status_code == 200:
        results = results.json()

        if 'results' in results.keys():
            collection = []
            for result in results['results']:
                r = requests.get(result['url'])
                collection.append(r.json())
            results = collection

        if type(results) is list:
            return render_template('%s.html' % page, results=results, title=page)
        else:
            return render_template('about-%s.html' % page, result=results)
    elif results.status_code == 404:
        return render_template('not_found.html')
    else:
        return render_template('error.html')


@app.route('/<page>/<name>/detail', methods=['GET'])
def about(page, name):
    if page not in pages:
        return redirect(url_for('index'))

    url = f"https://pokeapi.co/api/v2/{page}/{name}"

    results = requests.get(url)
    return render_template('about-%s.html' % page, result=results.json())


@app.route('/<path:dummy>')
def fallback(dummy=None):
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html')
