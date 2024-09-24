'''
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
'''


class Circle:

    def __init__(self, radius):
        self.radius = radius
        
    def computeArea(self):
        self.area = 3.14 * (self.radius ** 2)
        print(f"area = {self.area}")



circle1 = Circle(10)
circle1.computeArea()
