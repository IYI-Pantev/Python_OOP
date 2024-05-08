import re
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first.lower() + '.' + last.lower() + '@gmail.com'

    @property
    def first(self):
        return self._first
    @first.setter
    def first(self, value):
        if len(value) <=3:
            raise ValueError('Name must be greater than 3 characters.')
        self._first = value
    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@gmail.com"
    @email.setter
    def email(self, value):
        first, last, email, domain = re.split('[.@.]', value)
        self.first = first
        self.last = last
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @full_name.deleter
    def full_name(self):
        print('name deleted!')
        self.first = None
        self.last = None
    
emp_1 = Employee('John', 'Smith')
emp_1.first = 'Michael'
print(emp_1.full_name)
# print(emp_1.email)
print(emp_1.email)
emp_1.full_name = 'Sami Altman'
print(emp_1.email)
emp_1.email = 'sami.gptmaster@gmail.com'
print(emp_1.email)
# del emp_1.full_name
# print(emp_1.full_name)
print(emp_1.first)