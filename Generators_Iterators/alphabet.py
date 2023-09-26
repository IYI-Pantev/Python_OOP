import string

# Generate the lower case English letters

def letters():
    for c in string.ascii_lowercase:
        yield c

gen = letters()
for _ in range(1, 15):
    print(next(gen), end=" ")