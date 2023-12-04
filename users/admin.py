from django.contrib import admin
from django.contrib.admin import site

from products.admin import BasketAdmin
from users.models import EmailVerification, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    inlines = [BasketAdmin]
    extra = 0


# Register your models here.


class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'expiration']
    fields = ['code', 'user', 'expiration', 'created']
    readonly_fields = ['created']


site.register(EmailVerification, EmailVerificationAdmin)
site.register(User, UserAdmin)
