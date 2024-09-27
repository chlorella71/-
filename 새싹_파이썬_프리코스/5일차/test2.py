person = {'name':'ken',
          'age':3,
          'gender':'M'}

#데이터 조회
print(person['age'])

#데이터 삽입
person['address'] ='도봉'
print(person)

#데이터 수정
person['address']='동대문'

#
print(person['age'])
print(person.get('money', '그런 키는 없음'))

#상품의 이름이 '콜라', 가격이 '1800원', 재고가 '4개'인 데이터를 'product' 변수에 저장하기
product = {'이름': '콜라',
           '가격': 1800,
           '재고': 4}
print(product)

#product에 어떤 데이터 종류들이 저장되어 있는지 출력하기
print(product.keys())
print(product.values())
print(product.items())

#product를 활용하여 다음과 같은 형식으로 출력하기
for 키, 밸류 in product.items():
    print(f'{키} : {밸류}')

#콜라의 판매량이 3개일때, 이 데이터를 product에 반영하기
product['판매량'] = 3
product['재고'] -= 3

for 키, 밸류 in product.items():
    print(f'{키} : {밸류}')


