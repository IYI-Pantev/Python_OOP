import functools


def repeat(func=None, count=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result
    
        return wrapper
    if func:
        return decorator(func)
    else:
        return decorator


@repeat(count=3)
def say_hi():
    print('hi world')

say_hi()


