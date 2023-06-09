from project.vehicle import Vehicle


class Car(Vehicle):
    def drive(self):
        return 'driving...'

ford = Car()
print(ford.drive())