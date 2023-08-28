
# Interface Segregation Principle
# a class should not be forced to implement methods it doesn't need,
# and clients of an interface should only be required to know
# about the methods that are relevant to them.

from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass

class Manager(Worker, Eater):
    def work(self):
        print("Manager working")

    def eat(self):
        print("Manager eating")

class Engineer(Worker):
    def work(self):
        print("Engineer working")

class Chef(Eater):
    def eat(self):
        print("Chef eating")
