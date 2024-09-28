from collections import defaultdict

vending_machine = [
    {'name': 'cola', 'price': 1000, 'stock': 2},
    {'name': 'cider', 'price': 800, 'stock': 5},
    {'name': 'water', 'price': 500, 'stock': 10}
]

# print(vending_machine[0]['price'])

# 리스트에서 데이터들을 직접 꺼내기
# for beverage_info in vending_machine:
    # print(f'{beverage_info['name']}: {beverage_info['price']}원')

# 인덱스로 접근하기
# for idx in range(len(vending_machine)):
    # print(f'{vending_machine[idx]['name']}: {vending_machine[idx]['price']}원')

person = {'money' : int(input('가진돈: ')),
          'pocket' : defaultdict(int)}

while True:
    res = input('구매할까요? Y/N: ')
    if res == 'N':
        # 거스름돈 돌려주고 반복문 종료
        print(f'거스름돈: {person['money']}원')
        break

    elif res == 'Y':
        # 메뉴 보여주기
        for beverage_info in vending_machine:
            
            # stock > 0 인 메뉴만 출력
            if beverage_info['stock'] > 0:
                print(f'{beverage_info['name']}: {beverage_info['price']}')

        # 주문하기
        order = input('구매할 음료는?: ')

        # 목록을 뒤져서 해당 제품이 있는지 확인
        for idx in range(len(vending_machine)):
            if order == vending_machine[idx]['name']:
                
                # 재고가 없다면
                if vending_machine[idx]['stock'] <= 0:
                    print('재고 없음')

                # 돈이 부족하다면
                elif person['money'] < vending_machine[idx]['price']:
                    print('돈이 부족해요')
                    print(f'거스름돈: {person["money"]}원')
                
                # 돈이 충분하다면
                else:
                    print(f'{order}를 주문함')
                    
                    # person의 money 차감
                    person['money'] -= vending_machine[idx]['price']
                    print(f'거스름돈: {person["money"]}원')
                    
                    # vending_machine의 stock 차감
                    vending_machine[idx]['stock'] -= 1
                    
                    # person의 pocket에 order 추가
                    person['pocket'][order] += 1
                break
                
        # 목록에서 해당 제품을 못찾았다면
        else:
            print('주문 오류!')
            continue

print(vending_machine)
print(person['pocket'])
        