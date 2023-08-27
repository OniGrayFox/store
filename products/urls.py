from django.contrib import admin

from django.urls import path
from products.views import products_view

app_name = 'products'

urlpatterns = [

    path('', products_view, name='index')

]
