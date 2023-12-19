import stripe

from django.contrib import admin
from django.contrib.admin import site
from django.conf import settings

from .models import Basket, Product, ProductCategory



class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'image', 'category', 'stripe_product_price_id']
    fields = ['name', 'description', ('price', 'quantity'), 'image', 'category', 'stripe_product_price_id']
    search_fields = ['name', 'price', 'category']
    ordering = ['name']


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'created_timestamp']
    readonly_fields = ['created_timestamp']


site.register(ProductCategory, ProductCategoryAdmin)
site.register(Product, ProductAdmin)
