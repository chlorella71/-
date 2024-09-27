'''
while True:
    print('무한루프')
'''

#구구단 5단 출력
n = 1
while n < 6:
    for i in range(1,10):
        print(f'{n}*{i}={n*i}')
    n+=1

num = 1
while num <= 9:
    print(f'5 * {num} == {num*5}')
    num += 1

#40이하의 4의 배수를 출력하기
x = 1
while x <= 40:
    if x % 4 == 0:
        print(x)
    x += 1

i = 0
while True:
    i += 1
    num = 4 * i
    if num > 40:
        break
    print(num)

