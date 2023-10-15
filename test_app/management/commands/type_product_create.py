from abc import ABC
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from ...models import TypeProduct


class Command(BaseCommand, ABC):
    def handle(self, *args, **options):
        self.stdout.write('Создание типа продукта')
        type_product, created = TypeProduct.objects.get_or_create(type_product='Ноутбук')
        type_product, created = TypeProduct.objects.get_or_create(type_product='Телевизор')
        type_product, created = TypeProduct.objects.get_or_create(type_product='Телефон')
        type_product, created = TypeProduct.objects.get_or_create(type_product='Системный блок')
        type_product, created = TypeProduct.objects.get_or_create(type_product='Часы')
        type_product, created = TypeProduct.objects.get_or_create(type_product='Микрофон')
        self.stdout.write(self.style.SUCCESS('Успешно'))
