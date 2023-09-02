from django.db import models

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




