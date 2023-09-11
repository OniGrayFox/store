from django.contrib import admin

from django.urls import path
from products.views import products_view, basket_add, basket_remove

app_name = 'products'

urlpatterns = [

    path('', products_view, name='index'),
    path('category/<int:category_id>', products_view, name='category'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
