lst = [1,2,4,3,3,5,5,6,9,7]
for num in lst:
    if num != 1 and num != 4 and num != 5 and num != 7:
        print(num)

#단축 평가가 적용되어 위의 코드가 처리속도가 더 빠르다

for num in lst:
    if num not in [1, 4,5,7]:
        print(num)

#1~9까지의 자연수 중 제곱한 수가 10 이상 50 이하인 자연수의 리스트 출력하기
ans = []
for num in range(1, 10):
    if 10 <= num**2 <= 50:
        ans.append(num)
print(ans)