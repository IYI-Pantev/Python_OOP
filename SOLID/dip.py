# Dependency Inversion
#  Instead of high-level components depending directly on low-level components,
# both should depend on abstract interfaces or contracts. 

# ! Violating DIP:
class LightBulb:
    def turn_on(self):
        print("Light bulb turned on")

    def turn_off(self):
        print("Light bulb turned off")

class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()

bulb = LightBulb()
switch = Switch(bulb)
switch.operate()

# ? Adherence to DIP:
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Light bulb turned on")

    def turn_off(self):
        print("Light bulb turned off")

class Fan(Switchable):
    def turn_on(self):
        print("Fan turned on")

    def turn_off(self):
        print("Fan turned off")

class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.turn_on()

bulb = LightBulb()
fan = Fan()

switch1 = Switch(bulb)
switch2 = Switch(fan)

switch1.operate()
switch2.operate()


