from abc import ABC
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from ...models import Product, Shelving, TypeProduct, Order, PartOrder
from django.contrib.auth.models import User


class Command(BaseCommand, ABC):
    def handle(self, *args, **options):
        self.stdout.write('Создание типа продукта')
        type_product_1, created = TypeProduct.objects.get_or_create(type_product='Ноутбук')
        type_product_2, created = TypeProduct.objects.get_or_create(type_product='Телевизор')
        type_product_3, created = TypeProduct.objects.get_or_create(type_product='Телефон')
        type_product_4, created = TypeProduct.objects.get_or_create(type_product='Системный блок')
        type_product_5, created = TypeProduct.objects.get_or_create(type_product='Часы')
        type_product_6, created = TypeProduct.objects.get_or_create(type_product='Микрофон')
        self.stdout.write(self.style.SUCCESS('Успешно'))

        self.stdout.write('Создание стеллажей')
        shelf_1, created = Shelving.objects.get_or_create(letter_of_the_shelf='А')
        shelf_2, created = Shelving.objects.get_or_create(letter_of_the_shelf='Б')
        shelf_3, created = Shelving.objects.get_or_create(letter_of_the_shelf='Ж')
        shelf_4, created = Shelving.objects.get_or_create(letter_of_the_shelf='З')
        shelf_5, created = Shelving.objects.get_or_create(letter_of_the_shelf='В')
        self.stdout.write(self.style.SUCCESS('Успешно'))

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

        product_6, created = Product.objects.get_or_create(
            name=get_random_string(10),
            type_product=TypeProduct.objects.get(type_product='Микрофон'),
            shelving=Shelving.objects.get(letter_of_the_shelf='Ж'),
            quantity_products_in_stock=55,
        )
        self.stdout.write(self.style.SUCCESS('Успешно'))

        self.stdout.write('Создание пользователя')
        user_1 = User.objects.create_superuser(username='admin', password='admin')
        self.stdout.write('Создание заказа и добавление товара в заказ')
        order_10, created = Order.objects.get_or_create(user=user_1, number=10)
        order_10_product_1, created = PartOrder.objects.get_or_create(
            parent_order=Order.objects.get(id=order_10.id),
            product=Product.objects.get(id=product_1.id),
            quantity_products_in_order='2'
        )
        order_10_product_2, created = PartOrder.objects.get_or_create(
            parent_order=Order.objects.get(id=order_10.id),
            product=Product.objects.get(id=product_3.id),
            quantity_products_in_order='1'
        )
        order_10_product_3, created = PartOrder.objects.get_or_create(
            parent_order=Order.objects.get(id=order_10.id),
            product=Product.objects.get(id=product_6.id),
            quantity_products_in_order='1'
        )
        order_11, created = Order.objects.get_or_create(user=user_1, number=11)
        order_11_product_1, created = PartOrder.objects.get_or_create(
            parent_order=Order.objects.get(id=order_11.id),
            product=Product.objects.get(id=product_2.id),
            quantity_products_in_order='3'
        )
        order_14, created = Order.objects.get_or_create(user=user_1, number=14)
        order_14_product_1, created = PartOrder.objects.get_or_create(
            parent_order=Order.objects.get(id=order_14.id),
            product=Product.objects.get(id=product_1.id),
            quantity_products_in_order='3'
        )
        order_14_product_2, created = PartOrder.objects.get_or_create(
            parent_order=Order.objects.get(id=order_14.id),
            product=Product.objects.get(id=product_4.id),
            quantity_products_in_order='4'
        )
        order_15, created = Order.objects.get_or_create(user=user_1, number=15)
        order_15_product_2, created = PartOrder.objects.get_or_create(
            parent_order=Order.objects.get(id=order_15.id),
            product=Product.objects.get(id=product_5.id),
            quantity_products_in_order='1'
        )
        self.stdout.write(self.style.SUCCESS('Успешно'))
