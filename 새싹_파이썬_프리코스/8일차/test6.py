'''
추첨기는 다음과 같은 순서로 동작함
1. 프로그램을 실행과 동시에 5초의 카운트다운이 진행됨.
    1초가 흐를때 마다 '4초 남았습니다'와 같이 남은 시간을 출력
2. 카운트 다운이 종료되면, 1부터 45까지의 수 중 6개의 숫자를 무작위로 추출
3. 6개의 숫자를 오름차순으로 정렬하여 출력

sorted([]) : 오름차순으로 리스트를 정렬하는 함수
'''
import time, random

''' 내가 품
for i in range(5):
    print(f'{5-i}초 남았습니다')
    time.sleep(1)
lst = range(1,46)
print(sorted(random.sample(lst,6)))
'''

#1~45 숫자가 담긴 리스트 생성
nums = list(range(1, 46))
#nums = range(1, 46)

#반복을 돌면서
for sec in range(5, 0, -1):
    print(f'{sec}초 남았습니다.')
    time.sleep(1)

print(sorted(random.sample(nums, 6)))

