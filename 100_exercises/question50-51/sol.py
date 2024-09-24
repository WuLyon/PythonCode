'''
Define a class named American which has a static method called printNationality.

Hints: Use @staticmethod decorator to define class static method.
'''


class American:

    @staticmethod
    def printNationality():
        print("American")

    def __init__(self, name):
        self.name = name


class Newyork(American):
    pass


David = American('David')
David.printNationality()
American.printNationality()
Amy = Newyork('Amy')
Amy.printNationality()
Newyork.printNationality()
