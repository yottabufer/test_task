from django.contrib import admin
from .models import Shelving, TypeProduct, Product, Order, PartOrder


class AdminTypeProduct(admin.ModelAdmin):
    model = TypeProduct
    list_display = ('id', 'type_product')
    list_display_links = ('id', 'type_product')


class AdminShelving(admin.ModelAdmin):
    model = TypeProduct
    list_display = ('id', 'letter_of_the_shelf')
    list_display_links = ('id', 'letter_of_the_shelf')


class ProductInline(admin.TabularInline):
    model = Product.child_shelving.through
    verbose_name = 'Product'
    verbose_name_plural = 'Product'


class AdminProduct(admin.ModelAdmin):
    model = TypeProduct
    list_display = ('id', 'name', 'type_product', 'shelving', 'get_child_shelf', 'quantity_products_in_stock')
    list_display_links = ('id', 'name', 'type_product', 'shelving', 'get_child_shelf', 'quantity_products_in_stock')
    exclude = ('Product',)
    inlines = (ProductInline,)


class OrderInline(admin.TabularInline):
    model = PartOrder


class AdminOrder(admin.ModelAdmin):
    model = TypeProduct
    list_display = ('id', 'user', 'number')
    inlines = (OrderInline, )


admin.site.register(Shelving, AdminShelving)
admin.site.register(TypeProduct, AdminTypeProduct)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
