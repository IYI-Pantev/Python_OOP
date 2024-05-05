class Employee:

    RAISE_AMOUNT = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, salary: {self.pay})"
    def __str__(self):
        return f"Employee: {self.fullname()} - {self.email}"
    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())

    

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Michael', 'Davidov', 60000)
print(emp_1 + emp_2)
# print(emp_1)
# print('-------$')
# print(emp_2.__dict__)

