class Profile:
    username_min_length = 5
    username_max_length = 15
    
    pasword_min_length = 8
    min_uppercase_letters = 1
    min_digits = 1
    
    def __init__(self, username: str,  password: str):
        self.username = username
        self.password = password
      
    def __validate_pasword(self, pas):
        if len(pas) < self.pasword_min_length:
            raise ValueError("The pasword must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        if len([x for x in pas if x.isupper()]) < self.min_uppercase_letters:
            raise ValueError("The pasword must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        if len([x for x in pas if x.isdigit()]) < self.min_digits:
            raise ValueError("The pasword must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        
      
    @property    
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        username_len = len(value)
        if not Profile.username_min_length <= username_len <= Profile.username_max_length:
             raise ValueError('The username must be between 5 and 15 characters.')
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
    
    
my_profile = Profile("Nick_pythonista", "Mbbbbbb7")
print(my_profile)