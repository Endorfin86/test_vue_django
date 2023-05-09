from django.db import models

class Products(models.Model):
    title = models.CharField('Название', max_length=100)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"