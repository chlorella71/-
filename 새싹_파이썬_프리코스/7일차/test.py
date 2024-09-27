#1 ~100 중에 7의 배수의 개수를 출력하기
n = 1
cnt = 0
while n <= 100:
    if n % 7 == 0:
        cnt+=1
    n+=1
print(f'7의 배수의 개수: {cnt}개')

#lst = [1,2,4,3,3,5,5,6,9,7]일 때,
#원소가 1,4,5,7인 경우를 제외하고 출력
lst = [1,2,4,3,3,5,5,6,9,7]
lst2 = []
for i in lst:
    if i not in [1,4,5,7]:
        lst2.append(i)
print(lst2)

idx = 0
while idx < len(lst):
    if lst[idx] not in [1,4,5,7]:
        print(lst[idx], end=',')

    idx += 1
print()
