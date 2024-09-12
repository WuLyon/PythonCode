# Question: Define a class which has at least two methods: 
#   getString: to get a string from console input 
#   printString: to print the string in upper case. Also please include simple test function to test the class methods.

# Hints: Use init method to construct some parameters

class SOL():
    def __init__(self):
        self.str = ''

    def getString(self):
        self.str = input("input: ")

    def printString(self):
        print(self.str.upper())

sol = SOL()
sol.getString()
sol.printString()