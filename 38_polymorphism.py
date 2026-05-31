from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod # This decorator indicates that the method is abstract and must be implemented by any subclass of Shape.
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle): # Pizza is a subclass of Circle, which means it inherits the properties and methods of the Circle class. This allows us to treat a Pizza object as a Circle when calculating its area, while also adding additional attributes specific to a pizza, such as the topping.
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")
