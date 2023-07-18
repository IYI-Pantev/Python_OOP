class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ['bread'] + ingredients
        
    @classmethod
    def pepperoni(cls):
        return cls(['tomato sauce', 'parmesan', 'pepperoni'])
    
    
class Italian_pizza(Pizza):
    def __init__(self, ingredients):
        super().__init__(ingredients)
        self.ingredients = ['italian bread'] + ingredients
    
print(Pizza.pepperoni().__dict__)   
print(type(Pizza.pepperoni()))
print(Italian_pizza.pepperoni().__dict__)