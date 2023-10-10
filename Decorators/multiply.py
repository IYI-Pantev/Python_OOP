import functools

def multiply(times=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            final = result * times
            return final
        return wrapper
    return decorator


@multiply(times=3)
def add_ten(number):
    return number + 10

print(add_ten(4))
