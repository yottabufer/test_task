from abc import ABC
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from ...models import Shelving


class Command(BaseCommand, ABC):
    def handle(self, *args, **options):
        self.stdout.write('Создание стеллажей')
        shelf_1, created = Shelving.objects.get_or_create(letter_of_the_shelf='А')
        shelf_2, created = Shelving.objects.get_or_create(letter_of_the_shelf='Б')
        shelf_3, created = Shelving.objects.get_or_create(letter_of_the_shelf='Ж')
        shelf_4, created = Shelving.objects.get_or_create(letter_of_the_shelf='З')
        shelf_5, created = Shelving.objects.get_or_create(letter_of_the_shelf='В')
        self.stdout.write(self.style.SUCCESS('Успешно'))
