class cached:
    pass


@cached
def compute(x: int):
    print(f'calling {x}')
    return x * x