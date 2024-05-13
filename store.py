from products import Product

class Store:

    def __init__(self, product_list):
        self.list_of_products = product_list

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        item_count = 0
        for product in self.list_of_products:
            item_count += product.get_quantity()
        return item_count

    def get_all_products(self):
        return [product for product in self.list_of_products if product.is_active()]

    def order(self, shopping_list):

        price = float()

        #unpacks the list of tuples from shopping_list
        for product, quantity in shopping_list:
            product.buy(quantity)
            price += product.price * quantity

        return price