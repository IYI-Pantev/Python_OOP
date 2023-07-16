class Account:
    def __init__(self, id, balance, pin: int):
        self.__id = id
        self.balanace = balance
        self.__pin = pin
        
    def get_id(self, data):
        if data == self.__pin:
            return f"ID: {self.__id}"
        else:
            return "Wrong pin!"
    
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        else:
            return "Wrong pin!"
    
a = Account(1718, 200000, 3385)

print(a.get_id(3375))
print(a.get_id(3385))
print(a.balanace)
print(a.change_pin(3395, 0000))
print(a.change_pin(3385, 6933))
