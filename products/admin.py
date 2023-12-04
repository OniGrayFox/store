from django.contrib import admin
from django.contrib.admin import site

from .models import Basket, Product, ProductCategory


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'image', 'category']
    fields = ['name', 'description', ('price', 'quantity'), 'image', 'category']
    search_fields = ['name', 'price', 'category']
    ordering = ['name']


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'created_timestamp']
    readonly_fields = ['created_timestamp']


site.register(ProductCategory, ProductCategoryAdmin)
site.register(Product, ProductAdmin)
