from project.drink import Drink
from project.food import Food
from project.repository import ProductRepository

f = Food('banana')
d = Drink('coffee')
repo = ProductRepository()

repo.add(f)
repo.add(d)

print(repo.products)

print(repo)