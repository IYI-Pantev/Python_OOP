'''The idea here is that if the student has 5+ mark he/she has 40% semester discount.
But if we want to ad 20 % discount for 4+ mark
And we dont want to violate OCP we need extend not modificate'''

class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade
        
    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.6
        
class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        super().get_discount()
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.8
        
st = AdditionalDiscount('Peter', 100, 4.4)
        
print(st.get_discount())

        
