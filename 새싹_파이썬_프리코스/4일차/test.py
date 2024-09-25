S = str(input())
i = int(input())

print(S[i-1])

lst = [1,2,3,4,5]
for idx in range(5):
    lst[idx] += 1

print(lst)

# 1 ~ 100 중에서 7의 배수의 개수 출력하기
lst = list(range(1,101))
print(lst)

#답
cnt = 0
for num in range(1,101)
    if num % 7 ==0:
        cnt += 1
print(cnt)