class Profile:
    username_min_length = 5
    username_max_length = 15
    
    pasword_min_length = 8
    min_uppercase_letters = 1
    min_digits = 1
    
    def __init__(self, username: str,  password: str):
        self.username = username
        self.password = password
    @classmethod  
    def __validate_pasword(cls, pas):
        if len(pas) < cls.pasword_min_length:
            raise ValueError(f"The pasword must be {cls.pasword_min_length} or more characters with at least {cls.min_digits} digit and {cls.min_uppercase_letters} uppercase letter.")
        if len([x for x in pas if x.isupper()]) < cls.min_uppercase_letters:
            raise ValueError(f"The pasword must be {cls.pasword_min_length} or more characters with at least {cls.min_digits} digit and {cls.min_uppercase_letters} uppercase letter.")
        if len([x for x in pas if x.isdigit()]) < cls.min_digits:
            raise ValueError(f"The pasword must be {cls.pasword_min_length} or more characters with at least {cls.min_digits} digit and {cls.min_uppercase_letters} uppercase letter.")
        
      
    @property    
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        username_len = len(value)
        if not Profile.username_min_length <= username_len <= Profile.username_max_length:
             raise ValueError(f'The username must be between {self.username_min_length} and {self.username_max_length} characters.')
        self.__username = value
        
        
    @property    
    def password(self):
        return "".join('*' * len(self.__password))
    
    @password.setter
    def password(self, ps):
        self.__validate_pasword(ps)
        self.__password = ps
        
    def __str__(self):
        return f"You have a profile with username: {self.username} and password: {self.password}"
    
    
class Student(Profile):
    min_uppercase_letters = 3
        
    
    
    
    
my_profile = Profile("Nick_pythonista", "Mbbbbbb7")
print(my_profile)
print(my_profile.username)
print(my_profile.password)

#st = Student("Dj_bmn", "Mbbbbbb7")
