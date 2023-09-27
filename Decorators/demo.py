def f(x):
    z = 7 + x
    def internnal_f(y):
        return z + y
    internnal_f.initial_value = x
    
    return internnal_f

f1 = f(1)
print(f1)
print(f1.initial_value)

print(f1(4))

