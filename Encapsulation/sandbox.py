import re

email = "pe77er@gmail.com"

(name, mail, domain) = re.split('[@.]', email)

# print(name, mail, domain)

class Employee:

    def __init__(self, first, last):
        self._first = first
        self._last = last
        # self.email = first.lower() + '.' + last.lower() + '@gmail.com'

    # @property
    # def first(self):
    #     return self._first
    
emp_1 = Employee('John', 'Travolta')
emp_1.first = 'Michael'
print(emp_1.first)
print(emp_1.__dict__)