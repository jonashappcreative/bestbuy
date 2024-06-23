from products import NonStockedProduct


class Store:

    def __init__(self, product_list):
        self.list_of_products = product_list

    def get_all_products(self):
        return [product for product in self.list_of_products if product.is_active()]

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.list_of_products:
            if not isinstance(product, NonStockedProduct):
                total_quantity += product.get_quantity()
        return total_quantity

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.remove(product)

    def get_product_by_index(self, index):
        if 0 <= index < len(self.list_of_products):
            return self.list_of_products[index]
        else:
            return None

    def order(self, shopping_list):

        price = float()

        # unpacks the list of tuples from shopping_list
        for product, quantity in shopping_list:

            if product.get_promotion():
                #  print(product.promotion) DEBUG
                product.buy(quantity)
                price = product.promotion.apply_promotion(product, quantity)
            else:
                product.buy(quantity)
                price += product.price * quantity

        return price
