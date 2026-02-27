"""Part1:"""

class OutOfStockException(Exception):
    pass
class Product:
    def __init__(self, id, name, category, price,quantity_in_stock):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        if quantity_in_stock == 0:
            raise OutOfStockException("Quantity cannot be zero")
        self.quantity_in_stock = quantity_in_stock

    def add_stock(self, qty):
        self.quantity_in_stock += qty

    def remove_stock(self, qty):
        self.quantity_in_stock -= qty

    def get_value_in_stock(self):
        return self.quantity_in_stock


class InvalidEmailException(Exception):
    pass


class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        if not self.validate_email():
            raise InvalidEmailException("Invalid email address")

    def validate_email(self):
        """Returns True if email is valid, False otherwise."""
        if '@' not in self.email or '.' not in self.email.split('@')[-1]:
            return False
        return True

class Order:
    def __init__(self, id, customer, order_date):
        self.id = id
        self.customer = customer
        self.order_date = order_date
        self.items =[]

    def add_item(self, product, quantity):
        """Adds an item to the order."""
        order_item = OrderItem(product, quantity)
        self.items.append(order_item)

    def calculate_total(self):
        """Calculates the total price of all items in the order."""
        total = 0
        for item in self.items:
            total += item.get_subtotal()
        return total


class InvalidQuantityException(Exception):
    pass
class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        if quantity <= 0:
            raise InvalidQuantityException("Quantity must be positive")
        self.quantity = quantity

    def get_subtotal(self):
        """Calculates subtotal for this item."""
        return self.product.price * self.quantity



customer = Customer(1, "John Doe", "john@gmail.com")
product1 = Product(1, "Laptop", "iphone", 1000,2)
product2 = Product(2, "Mouse", "hardware" ,25, 2)

# Create order
order = Order(1, customer, "2024-02-08")
order.add_item(product1, 1)
order.add_item(product2, 2)

print(f"Total: ${order.calculate_total()}")






