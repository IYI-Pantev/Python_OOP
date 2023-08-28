#Liskov Substitution Principle
#if a class is a subclass of another class,
# it should be able to be used interchangeably with its superclass
# without causing unexpected behavior or violating the expected behavior of the program.

# ! violating example
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        return "Flying like a sparrow!"

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly!")

def make_bird_fly(bird):
    return bird.fly()

sparrow = Sparrow()
ostrich = Ostrich()

print(make_bird_fly(sparrow))  # Output: "Flying like a sparrow!"
print(make_bird_fly(ostrich))  # Raises an exception

# Adherence to LSP:
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        return "Flying like a sparrow!"

class Ostrich(Bird):
    def fly(self):
        return "Ostriches can't fly."

def make_bird_fly(bird):
    return bird.fly()

sparrow = Sparrow()
ostrich = Ostrich()

print(make_bird_fly(sparrow))  # Output: "Flying like a sparrow!"
print(make_bird_fly(ostrich))  # Output: "Ostriches can't fly."
