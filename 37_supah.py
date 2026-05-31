# super is a built-in function in Python that allows you to call methods from a parent class. It is commonly used in object-oriented programming to access and extend the functionality of a parent class in a child class. The super() function returns a temporary object of the superclass that allows you to call its methods.

class Shape:
    def __init__(self, color):
        self.color = color 
 
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
circle = Circle("red", 5)
square = Square("blue", 4)
triangle = Triangle("green", 6, 3)
