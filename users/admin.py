from django.contrib.admin import site
from django.contrib import admin

from users.models import User, EmailVerification
from products.admin import BasketAdmin



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
