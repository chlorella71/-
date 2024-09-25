점수 = int(input())
if 점수 <= 100 and 점수 >= 90:
    print('A')
elif 점수 <= 89 and 점수 >= 80:
    print('B')
elif 점수 <= 79 and 점수 >= 70:
    print('C')
elif 점수 <= 69 and 점수 >= 60:
    print('D')
else:
    print('F')