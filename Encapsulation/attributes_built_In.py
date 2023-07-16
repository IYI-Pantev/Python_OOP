class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    def info(self):
        return f"Name: {self.name}, Age: {self.age}"  
        
p = Person("Guman", 29)

c_name = input()
 
c_value = getattr(p, c_name)
if hasattr(c_value, '__call__'):
    print(c_value())
else:
    print(c_value)

    