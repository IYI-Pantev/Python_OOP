from project.car import Car

class Sportscar(Car):
    def race(self):
        return 'racing...'

lambo = Sportscar()
print(lambo.drive())
print(lambo.move())