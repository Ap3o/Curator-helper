from django.contrib import admin
from . import models


@admin.register(models.ClassPeriod)
class AdminParent(admin.ModelAdmin):
    list_display = ('topic', 'month',)


@admin.register(models.SpentClassPeriod)
class AdminParent(admin.ModelAdmin):
    list_display = ('class_period', 'content',)
