class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            print(product.display_info())

    def total_inventory_value(self):
        return sum(product.price * product.quantity for product in self.products)
    
    def remove_product(self, name):
        self.products = [product for product in self.products if product.name != name]