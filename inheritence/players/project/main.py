from project.elf import Elf
from project.hero import Hero

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(hero)
print('---next object---')
elf = Elf("E", 4)
print(elf)
print(elf.__class__.__bases__[0].__name__)