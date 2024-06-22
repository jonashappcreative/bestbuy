from abc import ABC, abstractmethod


class Promotion(ABC):

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        if quantity < 2:
            return product.price * quantity
        else:
            half_price_items = quantity // 2
            full_price_items = quantity - half_price_items
            return (full_price_items * product.price) + (half_price_items * product.price * 0.5)

    def show(self):
        return f"{self.name}"

class ThirdOneFree(Promotion):
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"{self.name}"

    def apply_promotion(self, product, quantity):
        free_third_items = quantity - (quantity // 3)
        full_price_items = quantity - free_third_items
        return full_price_items * product.price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def show(self):
        return f"{self.name}"

    def apply_promotion(self, product, quantity):
        discount_price = product.price * (1 - self.percent / 100)
        return discount_price * quantity
