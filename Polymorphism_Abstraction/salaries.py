class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def __gt__(self, other):
        return self.salary > other.salary
    
    
p1 = Person("NP", 4200)
p2 = Person("PR", 3200)

print(p1 > p2)