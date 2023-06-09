class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) > 0:
            return False
        else:
            return True

    # The join() method expects all the elements in the list to be strings
    def __str__(self):
        return f"{', '.join(str(x) for x in self.data[::-1])}"


s = Stack()
s.push(7)
s.push(9)
s.push(33)
s.push(34)
s.pop()
print(s.top())
print(s.is_empty())
print(s)
