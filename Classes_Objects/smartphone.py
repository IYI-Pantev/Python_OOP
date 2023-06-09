class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if self.is_on == False:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app, app_memory):
        if self.memory - app_memory > 0 and self.is_on:
            self.apps.append(app)
            self.memory -= app_memory
            return f'Installing {app}'
        elif self.memory - app_memory > 0 and not self.is_on:
            return f'Turn on your phone to install {app}'
        else:
            return f'Not enough memory to install {app}'

    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'


iphone = Smartphone(100)
print(iphone.install("Facebook", 60))
iphone.power()
print(iphone.install("Facebook", 60))
print(iphone.install("Messenger", 20))
print(iphone.install("Instagram", 40))
print(iphone.status())

