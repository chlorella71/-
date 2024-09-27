from collections import defaultdict

#아래 정보들을 자판기로 구조화히기
# 'name' : 'cola', 'price': 1000 , 'stock': 5
# 'name' : 'cider', 'price': 800 , 'stock': 7
# 'name' : 'water', 'price': 500 , 'stock': 10

vending_machine = [
    {'name' : 'cola', 'price': 1000 , 'stock': 5},
    {'name' : 'cider', 'price': 800 , 'stock': 7},
    {'name' : 'water', 'price': 500 , 'stock': 10}
]


#아래 정보들을 사람으로 구조화해보세요
#'money' : 10000
#'pocket' : defaultdict(int)

person = {
    'money' : 10000,
    'pocket' : defaultdict(int)
}


#자판기 동작 구현하기
while True:
    if person['money'] < 500:
        print('잔액이 부족합니다.')
        break

#1. 잔액을 보여주고, 주문 여부를 물음
    else:
        print(f'잔액 : {person['money']}')
        response = input('주문하시겠습니까? Y/N: ')

#2.1 주문을 하지 않으면 거스름돈을 돌려줌
    if response == 'N':
        print(f'거스름돈: {person['money']}원')
        break

 
# 2.2.1 주문을 하면 메뉴/가격 정보를 보여주고 주문을 받음
    elif response == 'Y':
        #메뉴/가격 정보를 출력
        for info in vending_machine:
            print(f'메뉴: {info['name']}, 가격: {info['price']}')
        
        #주문 받기(input())
        order = input('주문할 메뉴를 입력해주세요: ')


#2.2.2 반복문을 이용해 주문과 동일한 메뉴를 확인
        for idx in range(len(vending_machine)):
            if vending_machine[idx]['name'] == order and person['money'] >= vending_machine[idx]['price']:
            #돈이 충분하다면? => 출력/정산
                print(f'{order}를 주문합니다')
                vending_machine[idx]['stock'] -= 1
                person['money'] -= vending_machine[idx]['price']
                person['pocket'][vending_machine[idx]['name']] += 1
                print(f'잔액: {person['money']}')
                print(f'pocket: {person['pocket']}')
                break
            #돈이 없다면? => 출력/다시주문
            elif person['money'] < vending_machine[idx]['price']:
                print(f'잔액이 부족합니다. 다시 주문해주세요') 
                break

        else:
            print("잘못입력했습니다. 다시 주문해주세요")
            continue

#2.2.3 Y/N이 아닌 다른 응답이 오면 주문을 다시 받습니다
    else:
        print('잘못입력했습니다')
        continue

print(vending_machine)
print(person)