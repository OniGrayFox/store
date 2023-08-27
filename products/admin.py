from django.contrib import admin
from django.contrib.admin import site
from .models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'image', 'category']


site.register(ProductCategory, ProductCategoryAdmin)
site.register(Product, ProductAdmin)
