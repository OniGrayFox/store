from django.db import models
from users.models import User
# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=128, unique=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        verbose_name = "Категория продукта"
        verbose_name_plural = "Категории продуктов"

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=128)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0,  verbose_name="Количество товаров на складе")
    image = models.ImageField(upload_to='products_images', verbose_name="Изображение")
    category = models.ForeignKey(ProductCategory, verbose_name=ProductCategory._meta.verbose_name, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f'{self.name}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.product.price for basket in self)

    def total_quantity(self):

        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество Товара")
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()


    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    def __str__(self):
        return f"Корзина для {self.user.name} | Продукт: {self.product.name} "


    def sum(self):
        return self.product.price * self.quantity

