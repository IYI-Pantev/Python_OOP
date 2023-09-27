import random
import functools
import time

def compose(f, g, x):
    return f(g(x))
print("_---f(g(x))---_ :")
print("_---print(len(text))---_ :")
compose(print, len, 'Python')
print('- - - - - - -')

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        final_time = stop_time - start_time
        print(f"execute time: {final_time}")
        return result
    return wrapper

@timer
def random_power():
    def f(x):
        return x ** 2
    def g(x):
        return x ** 3
    def h(x):
        return x ** 4
    
    functions = [f, g, h]
    return random.choice(functions)

for i in range(5):
    p = random_power()
    print(p(3))