import threading
from App.models import User, Product, Order
from django.db import transaction
from django.core.management.base import BaseCommand


# Define data
users_data = [
    (1, 'Alice', 'alice@example.com'),
    (2, 'Bob', 'bob@example.com'),
    (3, 'Charlie', 'charlie@example.com'),
    (4, 'David', 'david@example.com'),
    (5, 'Eve', 'eve@example.com'),
    (6, 'Frank', 'frank@example.com'),
    (7, 'Grace', 'grace@example.com'),
    (8, 'Alice', 'alice@example.com'),
    (9, 'Henry', 'henry@example.com'),
    (10, '', 'jane@example.com'),
]

products_data = [
    (1, 'Laptop', 1000.00),
    (2, 'Smartphone', 700.00),
    (3, 'Headphones', 150.00),
    (4, 'Monitor', 300.00),
    (5, 'Keyboard', 50.00),
    (6, 'Mouse', 30.00),
    (7, 'Laptop', 1000.00),
    (8, 'Smartwatch', 250.00),
    (9, 'Gaming Chair', 500.00),
    (10, 'Earbuds', -50.00),
]

orders_data = [
    (1, 1, 1, 2),
    (2, 2, 2, 1),
    (3, 3, 3, 5),
    (4, 4, 4, 1),
    (5, 5, 5, 3),
    (6, 6, 6, 4),
    (7, 7, 7, 2),
    (8, 8, 8, 0),
    (9, 9, 1, -1),
    (10, 10, 11, 2),
]

class Command(BaseCommand):
    help = 'Insert data into users, products, and orders tables.'

    def insert_users(self):
        with transaction.atomic(using='users'):
            for user in users_data:
                User.objects.using('users').create(id=user[0], name=user[1], email=user[2])
        print("Users inserted successfully.")


    def insert_products(self):
        with transaction.atomic(using='products'):
            for product in products_data:
                Product.objects.using('products').create(id=product[0], name=product[1], price=product[2])
        print("Products inserted successfully.")


    def insert_orders(self):
        with transaction.atomic(using='orders'):
            for order in orders_data:
                Order.objects.using('orders').create(id=order[0], user_id=order[1], product_id=order[2], quantity=order[3])
        print("Orders inserted successfully.")

    def run_insertions(self):
        threads = []

        threads.append(threading.Thread(target=self.insert_users))
        threads.append(threading.Thread(target=self.insert_products))
        threads.append(threading.Thread(target=self.insert_orders))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print("All data inserted successfully.")

    def handle(self, *args, **kwargs):
        self.run_insertions()
