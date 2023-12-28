from django.db import models

# Create your models here.

class Part(models.Model):
    part_number = models.CharField('Номер детали', max_length=10, unique=True)
    name = models.CharField('Название детали', max_length=30)

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'

    def __str__(self):
        return self.part_number
