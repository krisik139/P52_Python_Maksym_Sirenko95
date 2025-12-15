class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(f"{self.name} - {self.price}")

class Customer:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Покупець {self.name}")

class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total(self):
        return self.product.price * self.quantity

    def info(self):
        total = self.get_total()
        print(f"{self.product.name} x {self.quantity} = {total} грн")

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product, quantity):
        item = OrderItem(product, quantity)
        self.items.append(item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_total

        return total

    def show_info(self):
        print("----------Zamovlenna----------")
        self.customer.info()
        for item in self.items:
            item.info()

        print(f"До сплати: {self.get_total()}")
        print("----------Zamovlenna----------")


pizza = Product("Піца Олександр", 359)
cola = Product("Кока Коля", 59)

#Може допишу

customer = Customer("Максім")

order1 = Order(customer)

order1.add_item(pizza)
order1.add_item(cola)
order1.show_info()