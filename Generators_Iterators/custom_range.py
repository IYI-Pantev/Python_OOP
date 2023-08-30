
# in this way the problem is that if we use nested loop
# we cant because the loop uses only one object data atribute
# class Custom_Range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current_number = self.start 
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current_number <= self.end:
#             value_to_return = self.current_number
#             self.current_number += 1
#             return value_to_return
#         else:
#             raise StopIteration
        
    
    
# ? the right way

class Custom_Range_Iterator:
    def __init__(self, custom_range):
        self.custom_range = custom_range
        self.current_number = self.custom_range.start
        
    def __next__(self):
        if self.current_number > self.custom_range.end:
            raise StopIteration
        
        value_to_return = self.current_number
        self.current_number += 1
        
        return value_to_return
    
class Custom_Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    # return an object with a method "__next__"
    def __iter__(self):
        return Custom_Range_Iterator(self)
        
    
ott = Custom_Range(1, 3)

for num in ott:
    print(num)
    
print("---------------")
print("--------Nested Loop--------")

for x in ott:
    print(f" --- Outer loop - {x} ---")
    for y in ott:
        print(f" --- Inner loop - {y} ---")