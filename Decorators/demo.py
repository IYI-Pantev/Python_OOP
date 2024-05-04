#Decorator
from functools import wraps

def decorator_func(original_func):
    @wraps(original_func)
    def wrapper_func(*args, **kwargs):
        print(f"wrapper func changed {original_func.__name__}")
        result = original_func(*args, **kwargs)
        return result.upper()
    return wrapper_func
    
# pythonic way
@decorator_func
def say_hi(name):
    return f'hello there {name}'

print(say_hi('james'))

# clear straightforward way
# def say_hi(name):
#     return f'hello there {name}'

# my_dec_func = decorator_func(say_hi)
# print(my_dec_func.__name__)
# # my_dec_func('john')
# print(my_dec_func('james'))

# def f(x):
#     z = 7 + x
#     def internnal_f(y):
#         return z + y
#     internnal_f.initial_value = x
    
#     return internnal_f

# f1 = f(1)
# print(f1)
# print(f1.initial_value)

# print(f1(4))

