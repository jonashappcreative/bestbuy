class Product:

    def __init__(self, name, price, quantity):

        if not name:
            print("Name can't be empty")
        if not price or price < 0:
            print("Price needs to be specified and must not be negative")
        if not quantity or quantity < 1:
            print("Quantity must be minimum one")

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
