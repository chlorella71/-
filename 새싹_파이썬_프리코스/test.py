print("hello")
print("hi")
# 개발자에게 문서화는 필수역량이다.

'''
따옴표 사이의 문장은 주석으로 처리된다.
'''

x, y = 100, 200
print(x, y)

c = x
x = y
y = c
print(x, y)

name = input('이름을 입력해주세요: ')
print('이름: ',name)

age = int(input('나이를 입력해주세요: '))
print(f'나이: {age}살')
print('age: ',age,'\nage의 type: ',type(age))

word1 = "Hello"
word2 = "World"
print(word1, word2, end="!\n")
print(word1, end=' ')
print(word2)

word1 = "chlorella71"
word2 = "gmail.com"
print(word1, end='@')
print(word2)

nickname = input('닉네임을 입력해주세요: ')
print(f'안녕하세요, {nickname}님!')

name=input('이름: ')
age=int(input('나이: '))
print(f'내 이름은 {name}이고 나이는 {age}살이야')