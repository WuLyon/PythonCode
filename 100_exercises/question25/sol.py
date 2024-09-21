'''
Question:
Define a class, which have a class parameter and have a same instance parameter

Hints:
Define a instance parameter, need add it in init method
You can init a object with construct parameter or set the value later
'''


class Person:
    name = 'Person'

    def __init__(self, name=None):
        self.name = name


person1 = Person('Lyon')
person2 = Person('Lua')
print(f'{Person.name} = {person1.name}')
print(f'{Person.name} = {person2.name}')
