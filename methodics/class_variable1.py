class Employee:
    NUM_OF_EMPS = 0
    RAISE_AMOUNT = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.NUM_OF_EMPS += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.fullname())
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.__dict__)
print(emp_1.__dict__)

emp_1.RAISE_AMOUNT = 1.05
print(emp_1.__dict__)
print(Employee.RAISE_AMOUNT)
print(emp_1.RAISE_AMOUNT)
print(emp_2.RAISE_AMOUNT)
print(f"current number of employees: {emp_2.NUM_OF_EMPS}")
