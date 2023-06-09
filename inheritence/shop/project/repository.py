from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        if product_name in self.products:
            return product_name
        return None

    def remove(self, product_name: str):
        if product_name in self.products:
            self.products.remove(product_name)

    def __repr__(self):
        result = ''

        for product in self.products:
            result += f'{product.name}: {product.quantity}'
            result += '\n'

        return result.strip()
