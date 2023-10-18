from abc import ABC
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from ...models import Product, Shelving, TypeProduct, Order, PartOrder
from django.contrib.auth.models import User
from collections import defaultdict


class Command(BaseCommand, ABC):

    def add_arguments(self, parser):
        parser.add_argument('order_number', nargs='+', type=str, help='Номера заказа')

    def handle(self, *args, **kwargs):
        out_dict = defaultdict(list)
        all_products_in_all_order = list()
        need_shelving_list = list()
        order_number = kwargs['order_number']
        for one_order in order_number:
            order = Order.objects.get(number=one_order)
            product_in_order = list(order.partorder_set.all())
            for _ in product_in_order:
                product = _.product_id
                all_products_in_all_order.append(product)
        for id_product in all_products_in_all_order:
            need_shelving = Product.objects.get(id=id_product).shelving
            need_shelving_list.append(need_shelving)
        unique_shelving_list = set(need_shelving_list)
        for num, key in enumerate(unique_shelving_list):
            for need_product in all_products_in_all_order:
                temp = Product.objects.get(id=need_product)
                if key == temp.shelving:
                    out_dict[key].append(temp.id)

        for key, value in out_dict.items():
            print(f'==============Стелаж {key}')
            for product in value:
                pass
                print(Product.objects.get(id=product).type_product)
                print(Product.objects.get(id=product).id)
                if Product.objects.get(id=product).child_shelving.values_list() is not None:
                    print('Доп.стелаж ', end='')
                    for qwe in Product.objects.get(id=product).child_shelving.values_list():
                        print(qwe[1], end=' ')
                    print()

