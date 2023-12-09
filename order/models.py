from django.db import models
from users.models import User

class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (DELIVERED, 'Доставлен'),
        (ON_WAY, 'В пути')
    )

    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    email = models.CharField(max_length=150, verbose_name="Email")
    address = models.CharField(max_length=150, verbose_name="Адрес доставки")
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ N{self.id}, {self.first_name} {self.last_name}"
