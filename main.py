import products
import promotions
from products import LimitedProduct, NonStockedProduct
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
        print(f"{index}. {product.show()}")
    print("------\n")


def generate_shopping_list(best_buy):
    print_product_list(best_buy)
    list_of_tuples = []
    product_choice = "LOOP_STARTER"
    active_products = best_buy.get_all_products()

    while product_choice != "":
        product_choice = input("Which product # do you want? ")
        if product_choice == "":
            break

        try:
            product_index = int(product_choice) - 1  # Adjust for 0-based indexing
            if 0 <= product_index < len(active_products):
                product = active_products[product_index]

                quantity = 0
                while quantity <= 0:
                    try:
                        quantity = int(input("What amount do you want? "))
                        if quantity <= 0:
                            print("Amount can't be zero or negative!")
                    except ValueError:
                        print("Please enter a valid number.")

                if isinstance(product, NonStockedProduct):
                    list_of_tuples.append((product_index, quantity))
                    print("Product added to list!")
                elif isinstance(product, LimitedProduct):
                    if quantity > product.maximum:
                        print(f"Sorry, the maximum quantity for {product.name} is {product.maximum}.")
                    else:
                        list_of_tuples.append((product_index, quantity))
                        print("Product added to list!")
                else:
                    if quantity > product.get_quantity():
                        print(f"Sorry, only {product.get_quantity()} of {product.name} is available.")
                    else:
                        list_of_tuples.append((product_index, quantity))
                        print("Product added to list!")
            else:
                print("Invalid product number.")
        except ValueError:
            print("Please enter a valid number.")

    return list_of_tuples


def make_order(best_buy):
    shopping_list_tuples = generate_shopping_list(best_buy)
    active_products = best_buy.get_all_products()
    shopping_list = []

    for item in shopping_list_tuples:
        index = item[0]
        quantity = item[1]

        # Append the corresponding product and quantity to the shopping list
        shopping_list.append((active_products[index], quantity))

    price_of_order = best_buy.order(shopping_list)
    print("\n******** Order Made ********")
    print(f"Your total order costs {price_of_order} EUR")


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
