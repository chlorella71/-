#2차원 리스트
'''
행(row)와 열(column)으로 이루어짐
행 : 세로
열 : 가로
'''

matrix = [[3, 7, 9],
          [4, 2, 6],
          [8, 1, 5]]
print(matrix)


print('원소에 접근하기: ')
#원소에 접근하기
print(matrix[0])
print(matrix[0][0])


print('원소 수정하기: ')
#원소 수정하기
matrix[1][2] = 100
print(matrix)


print('모든 원소에 접근하기: ')
#모든 원소에 접근하기 => for반복문 이용
for r in range(3):
    for c in range(3):
        print(matrix[r][c], end=", ")
    print()


print('행 우선순회: ')
#행 우선 순회 : 행을 먼저 순회함
matrix = [[3, 7, 9, 10],
          [4, 2, 6, 11],
          [8, 1, 5, 12]]
for r in range(3):
    for c in range(4):
        print(matrix[r][c], end=", ")
    print()


print('열 우선순회: ')
#열 우선 순회 : 열을 먼저 순회함
for c in range(4):
    for r in range(3):
        print(matrix[r][c], end=", ")
    print()






