def ranger(start, end):
    for num in range(start, end+1):
        yield num
        
print(list(ranger(1, 5)))