class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey): # Inheritance: Rabbit is a subclass of Prey, which means it inherits the properties and methods of the Prey class, which in turn inherits from the Animal class.    
    pass

class Hawk(Predator): # Similarly, Hawk is a subclass of Predator, which means it inherits the properties and methods of the Predator class, which in turn inherits from the Animal class.
    pass

class Fish(Prey, Predator): # Multiple inheritance: Fish can be both prey and predator which both are inheriting from the Animal class
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()  # Output: Bugs is eating
hawk.sleep()  # Output: Tony is sleeping
fish.eat()    # Output: Nemo is eating
fish.hunt()   # Output: Nemo is hunting