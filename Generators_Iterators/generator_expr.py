def squares(n):
    x = 1
    for i in range(n):
        yield x * x
        x += 1
        
    
for num in squares(3):
    print(num, end=" ")
    
print()

# another way 
squared_gen = (x ** 2 for x in range(1, 6))

for squared in squared_gen:
    print(squared)
