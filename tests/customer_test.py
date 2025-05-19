import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    c = Customer("John")
    assert c.name == "John"
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("J" * 20)

def test_customer_orders_and_coffees():
    c = Customer("Jane")
    coffee = Coffee("Espresso")
    c.create_order(coffee, 4.0)
    assert coffee in c.coffees()
    assert len(c.orders()) == 1

def test_most_aficionado():
    Customer.all_customers.clear()
    c1 = Customer("Amy")
    c2 = Customer("Ben")
    coffee = Coffee("Mocha")
    c1.create_order(coffee, 3.0)
    c2.create_order(coffee, 5.0)
    c2.create_order(coffee, 5.0)
    assert Customer.most_aficionado(coffee) == c2
