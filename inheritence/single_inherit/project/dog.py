from project.animal import Animal
# super dunder не прави наследяването, а извиква parent state
class Dog(Animal):

    def bark(self):
        return 'barking...'

dog = Dog()
print(dog.eat())
print(dog.bark())