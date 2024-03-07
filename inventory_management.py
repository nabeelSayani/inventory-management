from datetime import datetime

class Product:
    def __init__(self, product_id, name, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock

    def calculate_value(self):
        pass

class SimpleProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price

class PerishableProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price
        self.expiry_date = expiry_date

    def calculate_value(self):
        remaining_days = (self.expiry_date - datetime.now()).days
        discount = 0.1 if remaining_days <= 30 else 0
        return self.quantity_in_stock * self.unit_price * (1 - discount)

class DigitalProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, price):
        super().__init__(product_id, name, quantity_in_stock)
        self.price = price

    def calculate_value(self):
        return self.quantity_in_stock * self.price

# Example usage:
simple_product = SimpleProduct("SP001", "Book", 10, 15.99)
print("Total value of simple product:", simple_product.calculate_value())

perishable_product = PerishableProduct("PP001", "Milk", 20, 2.49, datetime(2024, 2, 28))
print("Total value of perishable product:", perishable_product.calculate_value())

digital_product = DigitalProduct("DP001", "Ebook", 50, 9.99)
print("Total value of digital product:", digital_product.calculate_value())
