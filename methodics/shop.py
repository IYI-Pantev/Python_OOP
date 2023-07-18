class Shop:
    def __init__(self, name: str, shop_type: str, capacity: int):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items_count = 0
        self.items = {}
        
     
    def _can_add_item(self):
        return self.items_count < self.capacity - 1
        
    def add(self, item):
        if not self._can_add_item():
            return "not enough capacity in the shop"
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1
        return f"{item} added to the shop"