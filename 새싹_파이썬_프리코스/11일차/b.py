'''
TMDB API활용 실습
a. 현재 상영중인 영화 중 평점(vote_average)이 가장 높은 영화
b. 현재 상영중인 영화 중 평점(vote_average)이 가장 높은 영화의 수익(revenue)찾기
c. 현재 상영중인 영화 중 평점(vote_average)이 7이상인 영화 나열
d. 현재 상영중인 영화를 평점(vote_average)순으로 정렬
- hint: list.sort(key=정렬기준)
e. 현재 상영중인 영화중 평점(vote_average)이 가장 높은 영화의 포스터이미지 조회
- hint: API 문서 참고하기
'''
import requests
import pprint

api_key = '049f6fcf28f01d62016557ff06626369'
BASE_URL = 'https://api.themoviedb.org/3/movie/'
path = 'now_playing'
infos = {'api_key': api_key,
          'language:': 'ko-Kr'}

response = requests.get(BASE_URL+path, params=infos)
data = response.json().get('results')

max_vote_average = 0
max_vote_average_movie = None

for movie in data:
    if max_vote_average < movie['vote_average']: 
        max_vote_average = movie['vote_average']
        max_vote_average_movie = movie

pprint.pprint(f'수익: ${data['revenue']}')