class Integer:
    def __init__(self, value):
        self.value = value
        
    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "float value is not float "
        return cls(int(float_value))
    
    @classmethod
    def from_roman(cls, value):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(value):
         if i+1<len(value) and value[i:i+2] in roman:
            num+=roman[value[i:i+2]]
            i+=2
         else:
            #print(i)
            num+=roman[value[i]]
            i+=1
        return cls(num)
        
    
    def __str__(self) -> str:
        return f"Value: {self.value}"
    


print(Integer.from_float(3.14).__dict__)
print(Integer.from_float("3.14"))
print(Integer.from_roman("CL"))