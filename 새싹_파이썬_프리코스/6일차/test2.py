people = [{'name' : 'jun',
          'age' : 15,
          'gender' : 'F'},
          {'name' : 'ken',
          'age': 20,
          'gender': 'M'},]

people = [
    {'name' : 'jun', 'age' : 15, 'gender' : 'F'},
    {'name' : 'ken', 'age' : 20, 'gender' : 'M'},
    {'name' : 'alex', 'age' : 3, 'gender' : '-'}
]

#이름이 alex인 사람에 대한 정보 출력
print(people[2])
for k, v in people[2].items():
    print(f'{k} : {v}')

#이름이 alex인 사람의 나이를 출력
print(f'나이 : {people[2]['age']}')

#사람들에 대한 정보를 각각 출력
for info in people:
    print(info)

for info in people:
    for k, v in info.items():
        print(f'{k} : {v}')
    print()

#이름을 활용하여 각 사람의 데이터에 쉽게 접근할 수 있도록 people변수 수정
people = [
    {'name':'jun', 'age': 15, 'gender': 'F'},
    {'name':'ken', 'age': 20, 'gender': 'M'},
    {'name':'alex', 'age': 3, 'gender': '-'}
]

people = {
    'jun' : {'name':'jun', 'age': 15, 'gender': 'F'},
    'ken' : {'name':'ken', 'age': 20, 'gender': 'M'},
    'alex' : {'name':'alex', 'age': 3, 'gender': '-'}
}

print(people['alex']['age'])

