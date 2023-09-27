def number_increment(numbers):

    def increase():
        nums = [i + 1 for i in numbers]
        return nums

    return increase()

print(number_increment([1, 2 ,3]))