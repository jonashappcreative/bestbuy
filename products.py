

class Product:

    def __init__(self, name, price, quantity, promotion=None):

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
        self.promotion = promotion

    def get_quantity(self):
        return float(self.quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity

        if self.quantity <= 0:
            self.active = False

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def is_active(self):
        return self.active

    def show(self):
        if self.promotion is None:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        else:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {self.promotion.show()}"

    def buy(self, buy_quantity):

        available_quantity = self.get_quantity()

        if available_quantity <= 0:
            print("Purchase quantity must be positive")
            return
            # raise ValueError("Purchase quantity must be positive")
        elif buy_quantity > available_quantity:
            raise ValueError(f"No soo many products available."
                   f"Currently we have {self.quantity} of {self.name} in stock.")
        else:
            self.set_quantity(available_quantity - buy_quantity)

            if self.promotion:
                total_price = self.promotion.apply_promotion(self, buy_quantity)
            else:
                total_price = self.price * buy_quantity

            return f"You bought {buy_quantity}x {self.name} for {total_price} EUR"


# Here we declare that the NonStockedProduct class inherits from the Product class
class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=1)  # quantity is a dummy
        self.quantity = "unlimited"

    # def show(self):
        #  Somehow get the Show text from the Main and add the Quantity: Unlimited as a string appendix
    #     return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {self.promotion.show()}"

    def buy(self, buy_quantity):
        total_price = 0
        if buy_quantity <= 0:
            print("Purchase quantity must be at least one")
            # raise ValueError("Purchase quantity must be at least one")

        elif self.promotion:
            total_price = self.promotion.apply_promotion(self, buy_quantity)
        else:
            total_price = self.price * buy_quantity
        return f"You bought {buy_quantity}x {self.name} for {total_price} EUR"


# Here we declare that the LimitedProduct class inherits from the Product class
class LimitedProduct(Product):
    def __init__(self, name, price, maximum):
        super().__init__(name, price, maximum)
        self.maximum = maximum

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: Maximum of {self.maximum} per order"

    def buy(self, buy_quantity):

        if buy_quantity <= 0:
            return f"Purchase quantity must be one, cancelled this request"
        if buy_quantity > self.maximum:
            return f"Cannot buy more than {self.maximum} per order"
        elif self.promotion:
            total_price = self.promotion.apply_promotion(self, buy_quantity)
        else:
            total_price = self.price * buy_quantity
        return f"You bought {buy_quantity}x {self.name} for {total_price} EUR"
