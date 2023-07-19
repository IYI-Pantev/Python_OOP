class Person:
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def get_population(cls):
        return cls.population
    
    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        return False
    