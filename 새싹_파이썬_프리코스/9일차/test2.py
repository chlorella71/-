#객체정의하기
class Person:
    #Person 객체의 공통된 정보와 행동(메서드) 설계하기
    #정보(변수) 변수 : 데이터를 담는 그릇
#    species = "인류"
    #행동(클래스안에서 함수가 정의되면 메서드임) 함수: 특정한 기능을 하는 집합체
#    def say(self): #메서드는 self를 받아야함?
#        print("안녕!") 

    #init(): 생성자 매직메서드
    def __init__(self, name, age, money):
        #인스턴스가 가지고 있는 정보를 표시
        self.name = name
        self.age = age
        self.money = money
        #인스턴스가 생성되었을때 발생할 코드
        print("응애!")

    def __str__(self):
        return f'내 이름은 {self.name}이고 나이는 {self.age}살이야'
    
    def say(self):
        print(f"안녕! 나는 {self.name}이야, 나는 {self.money}원 있어ㅎ")

#사람이름짓고
hui = Person("정희준", 29, 10000000000000)
print(hui)
print(hui.name)
print(hui.age)
print(hui.money)
#행동정의하기
hui.say() #.say() : 객체전용함수

#객체의 재사용성 - 객체 재사용하기
jun = Person("희준 정", 59, 1000000000000000)
jun.say()

'''
인스턴스 : 실제 만들어진 객체
hui, jun : 인스턴스

매직메서드 : 특별한 의미를 가지고 있는 메서드, 의미가 정해져있음
_ 2개로 시작해서 _ 2개로 끝남
init : 생성자 매직메서드
def __init__(self, 집어넣고싶은 정보1(ex. name), 정보2) -> None:
    pass
'''
