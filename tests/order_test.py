
import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_creation_and_properties():
    c = Customer("Liz")
    coffee = Coffee("Macchiato")
    order = Order(c, coffee, 5.5)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 5.5

def test_order_validations():
    c = Customer("Dan")
    coffee = Coffee("FlatWhite")
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
    with pytest.raises(TypeError):
        Order("NotCustomer", coffee, 4.0)
