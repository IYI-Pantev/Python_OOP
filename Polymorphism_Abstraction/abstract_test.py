from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# This will result in an error, as you cannot instantiate an abstract class directly.
# shape = Shape()

circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Area:", circle.area())
# print("Circle Perimeter:", circle.perimeter())

# print("Rectangle Area:", rectangle.area())
# print("Rectangle Perimeter:", rectangle.perimeter())