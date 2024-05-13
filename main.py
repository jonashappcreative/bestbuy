import products
from store import Store

def main():

    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)

    pixel = products.Product("Google Pixel 7", price=500, quantity=250)

    store = Store([bose, mac])
    store.add_product(pixel)

    price = store.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price} dollars.")


if __name__ == "__main__":
    main()
