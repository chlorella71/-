class Person:
    population = 0

    def __init__(self, name):
        Person.population += 1
        self.name = name
        print(f'응애! {self}이 태어났다')


    def __str__(self):
        return f'{self.name}, 사람'
    
    def command(self, cat):
        print(f'{cat.name}를 바라본다')
        while True:
            com = input('1. 부른다 2. 가까이가본다 3. 아무것도안한다 4. 츄르를꺼낸다: ')
            if com == '1':
                print(f'{cat.name}! 일로와')
                cat.come_here()
            elif com == '2':
                print(f'{cat.name}~')
                cat.run_away()
            elif com == '3':
                print(f'...({cat.name})')
                break
            elif com == '4':
                cat.run_into()
                com2 = input('1. 츄르를준다 2. 츄르를다시넣는다: ')
                if com2 == '1':
                    cat.eat()
                elif com2 == '2':
                    cat.run_away()
                
                


class Cat:
    population = 0
    
    def __init__(self, name):
        Cat.population += 1
        self.name = name
        self.like = 0
        print(f'야옹~ {self}가 있다')

    def __str__(self):
        return f'{self.name}, 고양이'
    
    def come_here(self):
        if self.like >= 10:
            print(f'뽈뽈뽈... {self.name}가 온다')
        else:
            print(f'...({self.name})')

    def run_away(self):
        print(f'뽈뽈뽈... {self.name}가 도망간다')

    def run_into(self):
        print(f'다다다! {self.name}가 헐레벌떡 뛰어온다')
        self.like += 1

    def eat(self):
        print(f'촵촵촵! {self.name}는 맛있게 먹는다')
        self.like += 5

class Persian(Cat):
    hair = 'long'

    def __init__(self, name):
        super().__init__(name)
        self.like = 10

    
hui = Person('희준')
jeje = Cat('제제')
kitty = Persian('이눔시키')
print(hui)
print(jeje)
print(f'사람: {Person.population}명')
print(f'고양이: {Cat.population}마리')

hui.command(jeje)
print(f'{jeje.name}의 호감도: {jeje.like}')
hui.command(kitty)