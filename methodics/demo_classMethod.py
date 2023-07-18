class Person:
    _min_name_legth = 2
    _max_name_legth = 15
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self._validate_name(value)
        self.__name = value
        
    @classmethod
    def _validate_name(cls, value):
        value_len = len(value)
        if value_len < cls._min_name_legth or  value_len > cls._max_name_legth:
            raise ValueError(f'Name must be between {cls._min_name_legth} and {cls._max_name_legth} characters.')
        
class Student(Person):
    _min_name_legth = 3

    
    
p = Person("Jo", 18)
st = Student("Yojiin", 22)        