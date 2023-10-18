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
