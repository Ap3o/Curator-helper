from django.db import models


# Create your models here.

# Отчёт
class Report(models.Model):
    content = models.CharField(max_length=2000, verbose_name="Содержание")
    start_at = models.DateField(verbose_name='Период от')
    end_at = models.DateField(verbose_name='Период до')

    class Meta:
        verbose_name_plural = "Отчёты"


# Родительские собрания
class ParentTeacherMeeting(models.Model):
    content = models.CharField(max_length=200, verbose_name='Содержание')
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name_plural = "Родительские собрания"


# Мероприятия воспитательной работы
class EducationalActivities(models.Model):
    activity = models.CharField(max_length=200, verbose_name='Мероприятие')
    date = models.DateField(verbose_name='Дата')
    note = models.CharField(max_length=1000, verbose_name='Примечание')

    class Meta:
        verbose_name_plural = "Мероприятия воспитальной работы"
