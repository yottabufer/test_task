from abc import ABC
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from ...models import Product, Shelving, TypeProduct


class Command(BaseCommand, ABC):
    def handle(self, *args, **options):
        self.stdout.write('Создание товаров')
        product_1, created = Product.objects.get_or_create(
            name=get_random_string(10),
            type_product=TypeProduct.objects.get(type_product='Ноутбук'),
            shelving=Shelving.objects.get(letter_of_the_shelf='А'),
            quantity_products_in_stock=55,
        )

        product_2, created = Product.objects.get_or_create(
            name=get_random_string(10),
            type_product=TypeProduct.objects.get(type_product='Телевизор'),
            shelving=Shelving.objects.get(letter_of_the_shelf='А'),
            quantity_products_in_stock=55,
        )

        product_3, created = Product.objects.get_or_create(
            name=get_random_string(10),
            type_product=TypeProduct.objects.get(type_product='Телефон'),
            shelving=Shelving.objects.get(letter_of_the_shelf='Б'),
            quantity_products_in_stock=55,
        )
        shelf_for_product_1 = Shelving.objects.get(letter_of_the_shelf='З')
        shelf_for_product_2 = Shelving.objects.get(letter_of_the_shelf='В')
        product_3.child_shelving.add(shelf_for_product_1)
        product_3.save()
        product_3.child_shelving.add(shelf_for_product_2)
        product_3.save()

        product_4, created = Product.objects.get_or_create(
            name=get_random_string(10),
            type_product=TypeProduct.objects.get(type_product='Системный блок'),
            shelving=Shelving.objects.get(letter_of_the_shelf='Ж'),
            quantity_products_in_stock=55,
        )

        product_5, created = Product.objects.get_or_create(
            name=get_random_string(10),
            type_product=TypeProduct.objects.get(type_product='Часы'),
            shelving=Shelving.objects.get(letter_of_the_shelf='Ж'),
            quantity_products_in_stock=55,
        )
        shelf_for_product_3 = Shelving.objects.get(letter_of_the_shelf='А')
        product_5.child_shelving.add(shelf_for_product_3)
        product_5.save()

        self.stdout.write(self.style.SUCCESS('Успешно'))
