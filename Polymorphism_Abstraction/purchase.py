class Purchase:
    def __init__(self, product_name, cost):
        self.product_name = product_name
        self.cost = cost
        
    def __add__(self, other):
        name = f"{self.product_name}, {other.product_name}"
        cost = self.cost + other.cost
        return Purchase(name, cost)

    
frst = Purchase('sofa', 650)
scnd = Purchase('table', 150)
print((frst + scnd).__dict__)    