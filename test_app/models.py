from django.db import models
from django.contrib.auth.models import User


class Shelving(models.Model):
    letter_of_the_shelf = models.CharField(max_length=5)
    objects = models.Manager()

    def __str__(self):
        return self.letter_of_the_shelf


class TypeProduct(models.Model):
    type_product = models.CharField(max_length=70)
    objects = models.Manager()

    def __str__(self):
        return self.type_product


class Product(models.Model):
    name = models.CharField(max_length=55)
    type_product = models.ForeignKey('TypeProduct', on_delete=models.CASCADE)
    shelving = models.ForeignKey('Shelving', on_delete=models.CASCADE, related_name='shelving')
    child_shelving = models.ManyToManyField('Shelving', blank=True, related_name='child_shelving')
    quantity_products_in_stock = models.PositiveSmallIntegerField()
    price = models.IntegerField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_child_shelf(self):
        child_list = self.child_shelving.get_queryset()
        child_str = ''
        for child in child_list:
            child_str += ', ' + child.letter_of_the_shelf
        return child_str.lstrip(', ')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(default=10)
    objects = models.Manager()

    def __str__(self):
        return str(self.number)


class PartOrder(models.Model):
    parent_order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_for_order')
    quantity_products_in_order = models.PositiveSmallIntegerField(default=1)
    objects = models.Manager()

    def __str__(self):
        return str(self.product.name)
