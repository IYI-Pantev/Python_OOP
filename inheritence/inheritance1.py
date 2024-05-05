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
    #class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.RAISE_AMOUNT = amount
    # constructor method | classmethod
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

class Developer(Employee):
    RAISE_AMOUNT = 1.054

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self.programming_language = programming_language

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

emp_str_1 = 'John-Doe-70000'

emp1 = Employee.from_string(emp_str_1)
dev1 = Developer('Jack', 'McDevon', 80000, 'C#')
dev2 = Developer('Dan', "O'Conor", 82000, 'Python')
# print(help(Developer))

#employee attributes and methods
# print(emp1.fullname())
# print(emp1.pay)
# print(emp1.RAISE_AMOUNT)
# emp1.RAISE_AMOUNT = 1.06

#developer attributes and methods
# print(dev1.fullname())
# print(dev1.email)
# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
# print(dev1.programming_language)
#manager attributes and methods
mng1 = Manager('Harry', 'Johnson', 90000, [])
print(mng1.fullname())
mng1.add_emp(dev1)
mng1.add_emp(dev2)
mng1.print_emps()

print(isinstance(dev1, Developer))
print(issubclass(Manager, Employee))