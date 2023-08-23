'''Liskov Substitution Principal
По-просто казано, ако даден клас e подклас на друг клас, той трябва да може да се използва взаимозаменяемо с неговия суперклас, без да предизвиква неочаквано поведение или да нарушава очакваното поведение на програмата.'''


# ! LSP violation
# class Bird:
#     def fly(self):
#         pass

# class Sparrow(Bird):
#     def fly(self):
#         return "Flying like a sparrow!"

# class Ostrich(Bird):
#     def fly(self):
#         raise Exception("Ostriches can't fly!")

# def make_bird_fly(bird):
#     return bird.fly()

# sparrow = Sparrow()
# ostrich = Ostrich()

# print(make_bird_fly(sparrow))  # Output: "Flying like a sparrow!"
# print(make_bird_fly(ostrich))  # Raises an exception
from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        return "Flying like a sparrow!"

class Ostrich(Bird):
    def fly(self):
        return "Ostriches can't fly."

def make_bird_fly(bird):
    return bird.fly()

sparrow = Sparrow()
ostrich = Ostrich()

print(make_bird_fly(sparrow))  # Output: "Flying like a sparrow!"
print(make_bird_fly(ostrich))  # Output: "Ostriches can't fly."
