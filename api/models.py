from django.db import models

class Item(models.Model):
    CURRENCY_CHOICES = (
        ('usd', 'usd'),
        ('eur', 'eur'),
        ('rub', 'rub'),
    )
    name = models.CharField(max_length=128, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveSmallIntegerField(verbose_name='Прайс')
    bool = models.BooleanField(verbose_name='Оплачивать', default=False)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, default='rub')

    class Meta:
        verbose_name_plural = 'Элемент'

    def __str__(self):
        return self.name
#
#                   РЕШИЛ ЗАДАЧУ БЕЗ ДОПОЛНИТЕЛЬНОЙ МОДЕЛИ, НО СОЗДАЛ ЕЕ ЧТО БЫ ПОКАЗАТЬ ПОНИМАНИЕ ManyToMany
#                                       В views добавлю сохранение в БД
#
# class Order(models.Model):
#     items = models.ManyToManyField(Item)
#
#     def __str__(self):
#         return self.items

#

