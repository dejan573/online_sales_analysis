from product import Product
from product_manager import ProductManager # type: ignore

if __name__ == "__main__":
    manager = ProductManager()
    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Phone", 500, 10)

    manager.add_product(product1)
    manager.add_product(product2)

    manager.display_products()
    print(f"Total inventory value: {manager.total_inventory_value()}")
    