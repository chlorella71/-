import requests
import pprint

URL = 'https://api.themoviedb.org/3/movie/popular?api_key=d007df33e3f03e1148dcaee79c3de63c&language=ko-Kr'

api_key = '049f6fcf28f01d62016557ff06626369'

BASE_URL = 'https://api.themoviedb.org/3/movie/'
path = 'now_playing'

infos = {'api_key': api_key,
          'language': 'ko-Kr'}

response = requests.get(URL)
# response = requests.get(BASE_URL+path, params=infos)

data = response.json()

pprint.pprint(data)


