class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print(f'Hello, my name is {self.name}!')
p = Person('Baram')
p.say_hi()