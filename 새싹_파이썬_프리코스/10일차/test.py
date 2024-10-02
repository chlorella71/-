class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1
        print(f"{self.name}, 천상천하 유아독존")


    def say(self):
        print(f'{self.name}, 너 자신을 알라')

    def __str__(self):
        return f'이름: {self.name}'
    
    def __del__(self):
        Person.population -= 1
        print("...")


hui = Person("희준")
jun = Person("정가")
hui.say()
print(f'인구수: {Person.population}')
print(hui)
del hui
print(Person.population)