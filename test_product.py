import pytest
from products import Product


def test_creating_product():
    """
    Test that creating a normal product works.
    """
    product_tested = Product("Windows Laptop", price=1000, quantity=50)
    assert product_tested.name == "Windows Laptop"
    assert product_tested.price == 1000
    assert product_tested.quantity == 50
    assert product_tested.is_active() is True


def test_creating_product_invalid_details_1():
    """
    Test that creating a product with invalid details
    (empty name, negative price) invokes an exception.
    :return:
    """
    with pytest.raises(ValueError, match="Name can't be empty") as execution_info:
        Product("", price=1450, quantity=100)
    assert str(execution_info.value) == "Name can't be empty"


def test_creating_product_invalid_details_2():
    """
    Test that creating a product with invalid details
    (empty name, negative price) invokes an exception.
    """
    with pytest.raises(ValueError) as execution_info:
        Product("Windows Laptop 2", price=-3, quantity=100)
    assert str(execution_info.value) == "Price needs to be specified and must not be negative"


def test_creating_product_invalid_details_3():
    """
    Test that creating a product with invalid details
    (empty name, negative price) invokes an exception.
    """
    with pytest.raises(ValueError) as execution_info:
        Product("Windows Laptop 3", price=700, quantity=0)
    assert str(execution_info.value) == "Quantity must be minimum one"


def test_product_becomes_inactive():
    """
    Test that when a product reaches 0 quantity, it becomes inactive.
    :return:
    """
    product = Product("Windows Laptop", price=1000, quantity=50)
    product.set_quantity(0)
    assert product.is_active() is False


def test_buy_modifies_quantity():
    """
    Test that product purchase modifies
    the quantity and returns the right output.
    :return:
    """
    product = Product("Windows Laptop Out", price=700, quantity=10)
    product.buy(5)
    assert product.quantity == 5


def test_buy_too_much():
    """
    Test that buying a larger
    quantity than exists invokes exception.
    """
    with pytest.raises(ValueError) as execution_info:
        product = Product("Windows Laptop Out", price=700, quantity=10)
        product.buy(11)
    assert (str(execution_info.value) == f"No soo many products available."
                                         f"Currently we have {product.quantity} of {product.name} in stock.")
