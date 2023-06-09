from Python_OOP.inheritence.food.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name


fruit = Fruit('Lemon', '2023-5-18')
print(fruit.name)
print(fruit.expiration_date)