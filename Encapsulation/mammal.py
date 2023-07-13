class PrivateClassVariable(Exception):
    pass

class Mammal:
    __kingdom = "animals"
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound
        
    def make_sound(self):
        return f"{self.name} makes {self.sound}"
    
    def get_kingdom(self):
        return Mammal.__kingdom
    
mam = Mammal("Dog", "Domestic", "Bark")
print(mam.make_sound())
print(mam.get_kingdom())
try:
    print(mam.__kingdom) 
except:
    raise PrivateClassVariable("can not access private")