from django.contrib import admin
from django.urls import path

from .views import OrderCreateView

app_name = 'order'

urlpatterns = [

    path('order-create', OrderCreateView.as_view(), name='order_create'),
   # path('order-success', )

]
