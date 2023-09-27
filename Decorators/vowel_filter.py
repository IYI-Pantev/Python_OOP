from functools import wraps

def is_vowel(ch):
    return ch in ('aeouiy' + 'aeouiy'.upper())

def vowel_decorator(func):

    @wraps(func)
    def wrapper():
        result = func()
        vowels = [x for x in result if is_vowel(x)]
        return vowels
    
    return wrapper

@vowel_decorator
def get_letters():
    return ['a', 'b', 'c', 'd', 'E']

print(get_letters())