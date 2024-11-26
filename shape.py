# pylint: disable=too-few-public-methods missing-module-docstring
class Shape:
    '''defines a shape'''
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def say_name(self):
        '''says the name of self'''
        return f"My name is {self.name}."

class Rectangle(Shape):
    '''defines a rectangle'''
    def __init__(self, color, name, width, height):
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        '''says the name of self'''
        return f"My name is {self.name} and I am a rectangle."

    def area(self):
        '''calculates the area of self'''
        return self.width*self.height

    def perimeter(self):
        '''calculates the perimeter of self'''
        return 2*(self.width + self.height)

class Circle(Shape):
    '''defines a circle'''
    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        '''says the name of self'''
        return f"My name is {self.name} and I am a circle."

    def area(self):
        '''calculates the area of self'''
        return 3.14 * self.radius ** 2

    def perimeter(self):
        '''calculates the perimeter of self'''
        return 2 * 3.14 * self.radius
