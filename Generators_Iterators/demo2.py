def my_generator(data):
    for item in data:
        yield item

my_list = [1, 2, 3, 4, 5]

print(next(my_generator(my_list)))
print(next(my_generator(my_list)))
