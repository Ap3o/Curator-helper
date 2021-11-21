from django.db import models


# Тематика классных часов по месяцам
class ClassPeriod(models.Model):
    topic = models.CharField(max_length=200, verbose_name='Тема собрания')
    MONTH_CHOICES = [
        ('Январь', 'Январь'),
        ('Февраль', 'Февраль'),
        ('Март', 'Март'),
        ('Апрель', 'Апрель'),
        ('Май', 'Май'),
        ('Июнь', 'Июнь'),
        ('Июль', 'Июль'),
        ('Август', 'Август'),
        ('Сентябрь', 'Сентябрь'),
        ('Октябрь', 'Октябрь'),
        ('Ноябрь', 'Ноябрь'),
        ('Декаберь', 'Декабрь')
    ]
    month = models.CharField(max_length=15, choices=MONTH_CHOICES, verbose_name='Месяц')

    class Meta:
        verbose_name_plural = "Тематика классных часов"


# Проведенные собрания
class SpentClassPeriod(models.Model):
    class_period = models.ForeignKey(ClassPeriod, on_delete=models.CASCADE, verbose_name='Тема собрания')
    content = models.CharField(max_length=500, verbose_name='Содержание')

    class Meta:
        verbose_name_plural = "Проведенные собрания"
