# "If it walks like a duck and it quacks like a duck, then it must be a duck." - This is the principle of duck typing in programming, which means that the type or class of an object is less important than the methods it defines and how it behaves. In Python, we can use duck typing to write flexible and reusable code without worrying about the specific types of objects we are working with.

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = True

    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)