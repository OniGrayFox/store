from django.contrib.admin import site
from django.contrib import admin

from users.models import User
from products.admin import BasketAdmin



class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    inlines = [BasketAdmin]
    extra = 0

site.register(User, UserAdmin)
# Register your models here.
