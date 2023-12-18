from django.contrib import admin
from django.urls import path

from .views import OrderCreateView, SuccessView, CancelView

app_name = 'order'

urlpatterns = [

    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order-success/', SuccessView.as_view(), name='order_success'),
    path('order-cancel/', CancelView.as_view(), name='order_cancel')

]
