from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="user_images", null=True, blank=True)

    class Meta:
        verbose_name = "Зарегистрированный пользователь"
        verbose_name_plural = "Зарегистрированные пользователи"

    def __str__(self):
        return f"{self.first_name} {self.email}"
