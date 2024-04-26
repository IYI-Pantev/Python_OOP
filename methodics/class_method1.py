class Employee:
    NUM_OF_EMPS = 0
    RAISE_AMOUNT = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + '.' + last + '@gmail.com' 
        Employee.NUM_OF_EMPS += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)
    #class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.RAISE_AMOUNT = amount
    # constructor method | classmethod
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_str_1 = 'John-Doe-70000'

# emp_data = emp_str_1.split('-')
# print(emp_data)
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
# Employee.set_raise_amt(1.05)

# print(Employee.RAISE_AMOUNT)
# print(emp_1.RAISE_AMOUNT)
# print(emp_2.RAISE_AMOUNT)