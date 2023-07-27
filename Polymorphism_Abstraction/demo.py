import math


class Shape:
    def area(self):
        pass
    
    
class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        result = self.radius * self.radius * math.pi       
        return f"{result:.1f}"
    
    
        
def calc_area(shape: Shape):
    print(shape.area())
    # print(shape.width, shape.height) # not good for polymorphism
    
calc_area(Rect(2, 5))        
calc_area(Circle(9))
r = Rect(3, 8)
print(f"is istance rect of shape: {isinstance(r, Shape)}")

# ? method overriding
class Person:
    def say_hi(self):
        print("Hello 1")
        
    def say_hi(self):
        print("Hello 2")
    
p = Person()   
p.say_hi()