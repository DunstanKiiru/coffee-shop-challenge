
import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_name_validation():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"
    with pytest.raises(ValueError):
        Coffee("A")

def test_coffee_customers_and_average():
    c1 = Customer("Tom")
    c2 = Customer("Jerry")
    coffee = Coffee("Americano")
    c1.create_order(coffee, 4.0)
    c2.create_order(coffee, 6.0)
    assert set(coffee.customers()) == {c1, c2}
    assert coffee.average_price() == 5.0
