class Person:
    def __init__(self, name, age):
        if not name:
            raise ValueError('Name cannot be None')
        self.set_name(name)
        # private/non-visible, accessible only from this class
        # self.__name = name
        # protected, accessible from within class and inherit objects
        self._age = age

    # public/visible

    def say_name(self):
        print(self.__name)

    # getter method
    def get_name(self):
        return self.__name

    # setter method
    def set_name(self, new_name):
        if not new_name:
            raise ValueError('Name cannot be None')

        if any([not x.isalpha() for x in new_name]):
            raise ValueError('Name can contain only letters')
        self.__name = new_name


p = Person('Nick', 28)
print(p._age)
print(p.__dict__)
print(p.get_name())
p.set_name("AliBaba")
print(p.get_name())
# p.set_name(None)
# bad practice
# print(p._Person__name)
# print(p.__name)
