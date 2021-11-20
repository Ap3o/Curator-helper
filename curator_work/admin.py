from django.contrib import admin
from . import models


@admin.register(models.Report)
class AdminParent(admin.ModelAdmin):
    list_display = ('content', 'start_at', 'end_at',)


@admin.register(models.EducationalActivities)
class AdminParent(admin.ModelAdmin):
    list_display = ('activity', 'date', 'note',)


@admin.register(models.ParentTeacherMeeting)
class AdminParent(admin.ModelAdmin):
    list_display = ('content', 'date', )
