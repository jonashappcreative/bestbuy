class Product:

    def __init__(self, name, price, quantity):

        if not name:
            print("Name can't be empty")
            raise ValueError("Name can't be empty")
        if not price or price < 0:
            print("Price needs to be specified and must not be negative")
            raise ValueError("Price needs to be specified and must not be negative")
        if not quantity or quantity < 1:
            print("Quantity must be minimum one")
            raise ValueError("Quantity must be minimum one")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return float(self.quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity

        if self.quantity <= 0:
            self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def is_active(self):
        return self.active

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, buy_quantity):

        available_quantity = self.get_quantity()

        if available_quantity <= 0:
            raise ValueError("Purchase quantity must be positive")
        elif buy_quantity > available_quantity:
            raise ValueError(f"No soo many products available."
                  f"Currently we have {self.quantity} of {self.name} in stock.")
        else:
            self.set_quantity(available_quantity - buy_quantity)
            return f"You bought {buy_quantity}x {self.name} for {self.price * buy_quantity} EUR"


# Here we declare that the NonStockedProduct class inherits from the Product class
class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=1) #quantity is a dummy
        self.quantity = "unlimited"

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited"

    def buy(self, buy_quantity):
        if buy_quantity <= 0:
            raise ValueError("Purchase quantity must be at least one")
        return f"You bought {buy_quantity}x {self.name} for {self.price * buy_quantity} EUR"


# Here we declare that the LimitedProduct class inherits from the Product class
class LimitedProduct(Product):
    def __init__(self, name, price, maximum):
        super().__init__(name, price, maximum) #quantity is a dummy
        self.maximum = maximum
        self.quantity = f"{self.maximum} per order"

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: Maximum of {self.maximum} per order"

    def buy(self, buy_quantity):

        if buy_quantity <= 0:
            print("Purchase quantity must be one, cancelled this request")
        elif buy_quantity == 1:
            return f"You bought {buy_quantity}x {self.name} for {self.price * buy_quantity} EUR"
        elif buy_quantity > 1:
            raise ValueError("Only one per order possible, added one instead.")
            return f"You bought {buy_quantity}x {self.name} for {self.price * buy_quantity} EUR"

