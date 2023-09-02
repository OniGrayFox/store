from django.contrib.admin import site


from users.models import User


site.register(User)
# Register your models here.
