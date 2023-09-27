import functools

def multiply(times=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            r = func(*args, **kwargs)
            f = r * times
            return f
        return wrapper
    return decorator


@multiply(times=3)
def add_ten(number):
    return number + 10

print(add_ten(4))