import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail

class User(AbstractUser):
    image = models.ImageField(upload_to="user_images", null=True, blank=True)
    is_varified = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Зарегистрированный пользователь"
        verbose_name_plural = "Зарегистрированные пользователи"

    def __str__(self):
        return f"{self.first_name} {self.email}"


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField(verbose_name="Дата жизни ссылки")

    class Meta:
        verbose_name = "Верификация пользователя"
        verbose_name_plural = "Верификации пользователей"

    def __str__(self):
        return f'Подверждение личности для {self.user.name} {self.user.email}'

    def send_verification_email(self):
        send_mail(
            '',
            'testing....',
            'from@example',
            [self.user.email]
        )