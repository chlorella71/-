#재료를 가지고 늑정 기능을 수행하고, 결과물을 뱉어주는 녀석

#def 함수이름(재료):
#   재료를 사용한 기능
#
#   return 결과물

# y = x + 1
def plus_one(x):
    y = x + 1

    return y
'''
def plus_one(x):
    return x+1
'''


# 함수를 실행(호출, call)
print(plus_one(int(input())))
print(plus_one(1))


#len() 리스트의 길이를 반환
#재료 : 리스트를 받아
#기능 : 받은 리스트의 길이를 계싼해
#결과물 : 계산한 길이를 반환
def my_len(lst):
    length=0
    for _ in lst:
        length+=1
    return length

my_lst = [1,2,3,4,5]
print(my_len(my_lst))
word='chlorella71'
print(my_len(word))


#sum() : ()안에있는 값모두 더해주는 함수 구현
#재료 : 리스트
#기능 : 리스트 안에 있는 숫자를 모두 더함
#반환값 : 모두 더해진 숫자
def my_sum(lst):
    sum_num = 0
    for num in lst:
        sum_num += num
    
    return sum_num

print(my_sum([1,2,3,4])) # 1+2+3+4
my_lst = [123,1234,534636,746574,14314]
print(my_sum(my_lst))
