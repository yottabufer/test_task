from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class AllOrderView(ListView):
    model = Order
    template_name = 'test_app/order_list.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shops'] = Product.objects.all()

        return context