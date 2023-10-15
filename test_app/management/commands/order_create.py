from abc import ABC
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from ...models import Product, Shelving, TypeProduct, Order


class Command(BaseCommand, ABC):
    def handle(self, *args, **options):
        self.stdout.write('Создание товаров')
        order_10, created = Order.objects.get_or_create(
            product=Product.objects.get(id=1),
            quantity_products_in_order=2,
        )