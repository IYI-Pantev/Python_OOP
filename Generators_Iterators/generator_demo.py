def custom_range(start, end):
    for x in range(start, end+1):
        yield x
        
for item in custom_range(1, 5):
    print(item)

# second demo

def char_range(text):
    for x in text:
        yield x
print("------------")
        
for c in char_range("fighter"):
    print(c)
    
print("------------")

class Person:
    def __init__(self, name):
        self.name = name
    # ? standart python scenario
    # generator function automatically calls iter and next
    def __iter__(self):
        for c in self.name:
            yield c

for x in Person("Good_Programmer"):
    print(x)