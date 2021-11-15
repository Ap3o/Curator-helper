from django.contrib import admin

from . import models


@admin.register(models.Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'home_address',)


@admin.register(models.Parent)
class AdminParent(admin.ModelAdmin):
    list_display = ('full_name', 'place_of_work', 'phone_number',)


@admin.register(models.Hobbies)
class AdminStudentsHobbies(admin.ModelAdmin):
    list_display = ('student', 'hobby',)


@admin.register(models.Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ('full_name', 'department',)


@admin.register(models.Performance)
class AdminPerformance(admin.ModelAdmin):
    list_display = ('student', 'subject', 'mark',)


@admin.register(models.Subject)
class AdminSubject(admin.ModelAdmin):
    list_display = ('name', 'teacher',)


@admin.register(models.AcademicPerformance)
class AdminAcademicPerformance(admin.ModelAdmin):
    list_display = ('student', 'subject', 'teacher', 'type_of_perfomance', 'mark')
