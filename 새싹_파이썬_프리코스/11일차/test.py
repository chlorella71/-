import requests
## terminal % pip3 install requests / requests 라이브러리 설치하기
## from pprint import pprint
import pprint
## 데이터를 편리하게 볼 수 있게 해주는 파이썬 라이브러리

URL = 'https://api.themoviedb.org/3/movie/popular?api_key=d007df33e3f03e1148dcaee79c3de63c&language=ko-Kr'

api_key = '049f6fcf28f01d62016557ff06626369'
# api_key = 'd007df33e3f03e1148dcaee79c3de63c'
# api_key를 변수화하여 재사용성 높이기

BASE_URL = 'https://api.themoviedb.org/3/movie/'
#URL을 분리하여 변수화하기
path = 'now_playing'
# path = 'popular'
# path를 분리하여 변수화하기, 다른 경로로 쉽게 바꿔볼 수 있게

infos = {'api_key': api_key,
          'language': 'ko-Kr'}
# params = {'api_key': 'd007df33e3f03e1148dcaee79c3de63c',
#           'language:': 'ko-Kr'}

response = requests.get(BASE_URL+path, params=infos)
# response = requests.get(URL)
# response = requests.get(URL, params=params)
# pprint.pprint(response.json())
## print(response.json())

data = response.json().get('results')
# data는 json형식으로 받을 수 있게 코드를 짜서 변수에 담기

max_vote_average = 0
max_vote_average_movie = None
# 내가 원하는 데이터를 담을 변수 생성

for movie in data:
    if max_vote_average < movie['vote_average']: 
        max_vote_average = movie['vote_average']
        max_vote_average_movie = movie
        # api문서 참고하여 용도에 따라 []안에 알맞게 입력

#원하는 데이터만 걸러서 출력해보기
# print(response.json()['results'][0]['original_title'])
# print(response.json()['results'][0]['vote_average'])
# print(max_vote_average_movie, max_vote_average)

##############################################

popular_movie_id = max_vote_average_movie['id']
path = str(popular_movie_id)

response = requests.get(BASE_URL+path, params=infos)
data = response.json()
pprint.pprint(f'수익: ${data['revenue']}')
# pprint.pprint(data)

##############################################

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

# a.
data = response.json().get('results')

for movie in data:
    if max_vote_average < movie['vote_average']: 
        max_vote_average = movie['vote_average']
        max_vote_average_movie = movie

pprint.pprint(data)


