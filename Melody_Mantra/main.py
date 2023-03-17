from flask import Flask, request, render_template, jsonify
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('tune.html')


@app.route('/spotify/search')
def search():
    query = request.args.get('query')
    data = search_spotify(query)
    result = {'success': True, 'data': data}
    return jsonify(result)


def search_spotify(query):
    url = "https://spotify81.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": "431293fbd2msh685c96f428f44c6p1f147ejsn46abd96a27ca",
        "X-RapidAPI-Host": "spotify81.p.rapidapi.com"
    }
    params = {"q": query, "type": "multi", "offset": "0", "limit": "10", "numberOfTopResults": "5"}

    response = requests.get(url, headers=headers, params=params)
    results = json.loads(response.content)
    album = results.get('albums', {})
    try:
        if album:
            item = album.get('items', [])
            
            data = []
            for i in item:
                data.append(i.get('data', {}))

            artist = []
            for j in data:
                artist.append(j.get('artists', {}))

            items1 = []
            for k in artist:
                items1.append(k.get('items', {}))

            profile = []
            for g in items1:
                profile.append(g[0].get('profile', {}).get('name', {}))
            return profile
        else:
            return {'error': f'Missing required key'}
    except KeyError as e:
        return {'error': f'Missing required key{e}'}


if __name__ == '__main__':
    app.run(debug=True, port=977)
