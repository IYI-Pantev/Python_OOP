class Employee:
    NUM_OF_EMPS = 0
    RAISE_AMOUNT = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
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
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2024, 4, 26)

print(my_date.weekday())

print(Employee.is_workday(my_date))