import requests
from pprint import pprint
URL = 'https://api.themoviedb.org/3/movie/popular?api_key=d007df33e3f03e1148dcaee79c3de63c&language=ko-Kr'
api_key = "41e24eb5ac04fe4a069357648e2589a6"
BASE_URL = 'https://api.themoviedb.org/3/movie/'
path = 'now_playing'
infos = {'api_key': api_key,
          'language': 'ko-Kr'}
response = requests.get(BASE_URL+path, params=infos)
data = response.json().get('results')
print(data)