from django.core.management.base import BaseCommand
from App.models import User, Product, Order
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "distributed_system.settings")
django.setup()

class Command(BaseCommand):
    help = 'Check and print all data from users, products, and orders databases.'

    def handle(self, *args, **kwargs):
        users = User.objects.using('users').all()
        print("Users in the 'users' database:")
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

        products = Product.objects.using('products').all()
        print("\nProducts in the 'products' database:")
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")

        orders = Order.objects.using('orders').all()
        print("\nOrders in the 'orders' database:")
        for order in orders:
            print(f"ID: {order.id}, User ID: {order.user_id}, Product ID: {order.product_id}, Quantity: {order.quantity}")

        print("\nData checked successfully.")
