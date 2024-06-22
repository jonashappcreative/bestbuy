import products
from store import Store


def start(best_buy):
    list_of_commands = [
        "1. List all products in store",
        "2. Show total amount in store",
        "3. Make an order",
        "4. Quit"
    ]

    is_running = True

    while is_running:
        print("\n   Store Menu\n   ----------")
        for command in list_of_commands:
            print(command)

        try:
            print("")
            user_choice = int(input("Please choose a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 < user_choice <= len(list_of_commands):
            if user_choice == 1:
                print_product_list(best_buy)
            elif user_choice == 2:
                print(f"The store currently has {best_buy.get_total_quantity()} items in stock")
            elif user_choice == 3:
                make_order(best_buy)
            elif user_choice >= 4:
                is_running = False
                print("Exiting...")


def print_product_list(best_buy):
    print("------")
    product_list = best_buy.get_all_products()
    for index, product in enumerate(product_list, start=1):
        print(f"{index}. {product.name}, Price {product.price} EUR, Quantity: {product.quantity}")
    print("------\n")


def generate_shopping_list(best_buy):

    print_product_list(best_buy)

    list_of_tuples = []

    product_choice = "LOOP_STARTER"

    while product_choice != "":

        product_choice = input("Which product # do you want? ")
        if product_choice != "":
            quantity = input("What amount do you want? ")
            print("Product added to list!")
            print("")
            tuple_choice = product_choice, quantity
            list_of_tuples.append(tuple_choice)

    return list_of_tuples


def make_order(best_buy):

    list_of_tuple = generate_shopping_list(best_buy)
    active_products = best_buy.get_all_products()

    shopping_list = []

    for item in list_of_tuple:

        # Convert index and quantity from string to int and adjust index
        index = int(item[0]) - 1  # Subtract 1 for 0-based indexing
        quantity = int(item[1])

        # Append the corresponding product and quantity to the shopping list
        shopping_list.append((active_products[index], quantity))

    price_of_order = best_buy.order(shopping_list)
    print("\n******** Order Made ********")
    print(f"Your total order costs {price_of_order} EUR")


def main():

    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
