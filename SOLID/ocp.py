# The OCP/Open-Close Principle states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.

# ! OCP violation

# class Shape:
#     def __init__(self, type):
#         self.type = type

# class AreaCalculator:
#     def calculate_area(self, shape):
#         if shape.type == "circle":
#             return 3.14 * shape.radius * shape.radius
#         elif shape.type == "rectangle":
#             return shape.width * shape.height
        # Adding more shapes here would require modifying this class
        
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class AreaCalculator:
    def calculate_area(self, shape):
        return shape.calculate_area()
