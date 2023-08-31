class Reverser:
    def __init__(self, reverse_iterator):
        self.reverse_iterator = reverse_iterator
        self.index = -1
        
    def __next__(self):
       if abs(self.index) > len(self.reverse_iterator.iterable_list):
           raise StopIteration
       
       value_to_return = self.reverse_iterator.iterable_list[self.index]
       
       self.index -= 1
       
       return value_to_return
       
        

class Reverse_Iterator:
    def __init__(self, iterable):
        self.iterable_list = list(iterable)
        self.index = -1
        
    def __iter__(self):
        return Reverser(self)


rev = Reverse_Iterator([1, 2, 3, 4, 5])

for i in rev:
    print(i)        
    