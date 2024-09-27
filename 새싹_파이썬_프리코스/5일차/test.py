#리스트에서 1, 4, 5, 7을 제외한 숫자 출력
lst = [1,2,4,3,3,5,5,6,9,7]
for num in lst:
    if num != 1 and num != 4 and num != 5 and num != 7:
        print(num, end=' ')
print()

#단축 평가가 적용되어 위의 코드가 처리속도가 더 빠르다

for num in lst:
    if num not in [1, 4,5,7]:
        print(num, end=' ')
print()

#1~9까지의 자연수 중 제곱한 수가 10 이상 50 이하인 자연수의 리스트 출력하기
ans = []
for num in range(1, 10):
    if 10 <= num**2 <= 50:
        ans.append(num)
print(ans)

# n을 입력받아 소수인지 판단
n = int(input('숫자를 입력하세요: '))
for i in range(2,n):
    if n % i == 0:
        print(f"{n}은(는) 소수가 아닙니다")
        break
else:
    print(f"{n}은(는) 소수입니다")

# 2의 배수 혹은 3의 배수를 제외하고 1~30까지 숫자를 출력하시오
for i in range(1, 31):
    if i % 2 == 0:
        continue
    if i % 3 == 0:
        continue
    print(i, end=' ')

print()



