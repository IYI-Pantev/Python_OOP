#Decorators
from functools import wraps

def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2} sec")
        return result
    return wrapper

import time

@my_timer
def info(name, age, city):
    time.sleep(1)
    print(f"name: {name}, age: {age}, city: {city}")


info('john', 29, 'new york')