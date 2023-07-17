class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)
    @staticmethod
    def multiply(*args):
        r = 1
        for x in args:
            r *= x 
            
        return r
    @staticmethod
    def devide(initial, *args):
        r = initial
        for x in args:
            r /= x 
            
        return r
    @staticmethod
    def subtract(initial, *args):
        r = initial
        for x in args:
            r -= x 
            
        return r
    
print(Calculator.add(4, 7, 2))
calc = Calculator()
print(calc.add(1, 2))