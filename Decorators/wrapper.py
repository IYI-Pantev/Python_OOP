from functools import wraps

# construct my decorator
def uppercase(func):
    def wrapper():
        result = func()
        uppercase_result = result.upper()
        return uppercase_result


    return wrapper

def say_hi():
    return 'hello there'
# 1st way
decorate = uppercase(say_hi)
print(decorate())

# second way is the 'Pythonic way'

@uppercase
def say_bye():
    return 'bye mate'

print(say_bye())