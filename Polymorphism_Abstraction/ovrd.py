
# ! Overloading Built-in Methods __smth__
class Items:
    def __init__(self):
        self._items = []
        
        
    def add_item(self, item):
        self._items.append(item)
    
    # override using dunder method    
    def __len__(self):
        return len(self._items)
    
    def __str__(self) -> str:
        return str(self._items)
    
    def __add__(self, other):
        result = Items()
        [result.add_item(item) for item in self._items]
        [result.add_item(item) for item in other._items]
        return result
    
ii = Items()    
ii.add_item(1)
ii.add_item(1)
ii.add_item(1)
# ? len() now works with Class
print(len(ii))

i2 = Items()
i2.add_item(-1)

i_result = ii + i2
print(i_result)