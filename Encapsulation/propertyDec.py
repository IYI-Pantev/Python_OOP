class House:
    def __init__(self, price):
        self._price = price
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter valid price.")
            
    @price.deleter
    def price(self):
        del self._price
        
        
villa = House(570000.00)
print(villa.price)
villa.price = - 125
print(villa.price)
villa.price = 650000.00
print(villa.price)