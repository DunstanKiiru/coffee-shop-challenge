from customer import Customer
from coffee import Coffee

c1 = Customer("Alice")
c2 = Customer("Bob")
c3 = Customer("Charlie")

latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")

c1.create_order(latte, 4.0)
c2.create_order(latte, 5.0)
c2.create_order(latte, 5.0)
c3.create_order(cappuccino, 3.0)

print(f"Aficionado for Latte: {Customer.most_aficionado(latte).name}")  # Should be Bob
