from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sensors_amount(self):
        pass


class WarRobot(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def fire(self, weapon):
        return f"{weapon} is firing"
    
class Drone(WarRobot):
    def fire(self, weapon):
        return f"{weapon} is firing at the target"
    
class Medical_Robot(Robot):
    @property
    def sensors_amount(self):
        return 10
    
class Chef_Robot(Robot):
    @property
    def sensors_amount(self):
        return 7

med_robo = Medical_Robot("Da Vinci")
chefo_robo = Chef_Robot("Passio")
war_robo = Drone("Invictus")
# print(med_robo.name)
# print(med_robo.sensors_amount)
robots = [med_robo, chefo_robo, war_robo]
for robot in robots:
    if isinstance(robot, Robot):
        print(robot.name, robot.sensors_amount)
    if isinstance(robot, WarRobot):
        print(robot.name, robot.fire("laser"))
