from django.urls import path
from .views import AllOrderView

urlpatterns = [
    path('', AllOrderView.as_view(), name='all_product'),


]