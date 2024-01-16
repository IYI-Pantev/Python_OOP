# singleton pattern
# creational design pattern that ensures that a class has only one instance

# 1-st way
# class House_Pure_Singleton:
#     _instance = None
    
#     def __init__(self, floor, pool):
#         self.floor = floor
#         self.pool = pool
#         House_Pure_Singleton._instance = self

#     @classmethod    
#     def get_instance(cls):
#         return cls._instance

# more pythonic way
from dct_mxn import StrDictMixin
import functools

def singleton(cls):
    istances = []
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not istances:
            istances.append(cls(*args, **kwargs))
        return istances[0]
    return wrapper

@singleton
class House(StrDictMixin):
    def __init__(self, floor, pool):
        self.floor = floor
        self.pool = pool

print(House(3, True))
print(House(2, False))
print(House(1, True) == House(2, False))


        


        

