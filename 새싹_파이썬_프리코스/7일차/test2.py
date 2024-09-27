#python library : 가져와서 쓰는 기능
from collections import defaultdict

# 집계 알고리즘
votes = ['a', 'a', 'b', 'b', 'c', 'a', 'b', 'a', 'b', 'c', 'a', 'a', 'b', 'c']

# 집합으로 집계하기
result_dict = {
    'a' : 0,
    'b' : 0,
    'c' : 0
}


# 집합의 원소가 많은 경우
result_dict2 = {}

for vote in votes:
    # 처음 나온 표라면 생성
    if vote not in result_dict2:
        result_dict2[vote] = 1
    
    # 아니라면 1 증가
    else:
        result_dict2[vote] += 1
print(result_dict2)


#library 사용하기
result_dict3 = defaultdict(int)

for vote in votes:
    result_dict3[vote] += 1

print(result_dict3)


# 리스트로 집계하기
for vote in votes:
    result_dict[vote] += 1
print(result_dict)


result_lst =[0,0,0]

for vote in votes:
    if vote == 'a':
        result_lst[0] +=1
    elif vote == 'b':
        result_lst[1] +=1
    else:
        result_lst[2] +=1
print(result_lst)


# 내가 품
cnt_a = 0
cnt_b = 0
cnt_c = 0
for i in votes:
    if i == 'a':
        cnt_a +=1
    elif i == 'b':
        cnt_b +=1
    elif i == 'c':
        cnt_c +=1
print(f'a : {cnt_a}, b : {cnt_b}, c : {cnt_c}')


# 최대값/최소값 구하기
nums = [594, 12, 3, 3151, 213, 212, -123, 23, -2, 457, 264, 89, 2543, 2333, 4536, -243]

left = nums[0]
right = left
for i in nums:
    if i > left:
        left = i

for i in nums:
    if i < right:
        right = i
print(f'최대값 : {left}, 최소값 : {right}')

#float("INF") : 무한대의 최대값
#-float("INF") : 무한대의 최소값

left = float("INF")


for right in nums:
    if right < left:
        left = right
print(left)
