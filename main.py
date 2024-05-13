import products
from store import Store

def main():

    """
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)

    pixel = products.Product("Google Pixel 7", price=500, quantity=250)

    store = Store([bose, mac])
    store.add_product(pixel)

    price = store.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price} dollars.")
    """

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                   ]

    '''print(product for product in product_list)
    print(type(product_list))
    print(type(product for product in product_list))'''


    store = Store(product_list)

    # Name differently than the imported products class!
    active_products = store.get_all_products()

    # Here we print the ammount of items in the store
    print(f"The store currently has {store.get_total_quantity()} items in stock")

    # Here we are referencing the list of products by using their (index[x], quantity)
    price_of_order = store.order([(active_products[0], 1), (active_products[1], 2)])
    print(f"Your total order costs {price_of_order} EUR")

    print(f"The store now has {store.get_total_quantity()} items in stock")


if __name__ == "__main__":
    main()
