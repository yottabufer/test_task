from django.db import models


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
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity_products_in_order = models.PositiveSmallIntegerField()
    objects = models.Manager()

    def __str__(self):
        return self.product


