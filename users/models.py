import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

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
        return f'Подверждение личности для {self.user.username} {self.user.email}'

    def send_verification_email(self):
        link = reverse('users:verify', kwargs={'email': self.user.email, 'code': self.code})
        ver_link = f"{settings.DOMAIN_NAME}{link}"
        subject = f"Подтверждение учетной записи для {self.user.username}"
        message = f"Для подтверждения учетной записи для {self.user.username} перейдите по ссылке: {ver_link}"
        send_mail(
            subject=subject,
            message=message,
            from_email='from@example',
            recipient_list=[self.user.email],
            fail_silently=True,
        )

    def is_expired(self):
        return True if timezone.now() >= self.expiration else False