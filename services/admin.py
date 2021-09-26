from django.contrib import admin
from . import models


@admin.register(models.UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    list_display = ('user', 'avatar', )
