from django.db import models


# Студент
class Student(models.Model):
    full_name = models.CharField(max_length=120, verbose_name="ФИО")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    home_address = models.CharField(max_length=200, verbose_name="Домашний адрес")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Студенты"


# Родитель
class Parent(models.Model):
    full_name = models.CharField(max_length=120, verbose_name="ФИО")
    place_of_work = models.CharField(max_length=200, verbose_name="Место работы")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Родители"


# Родители студентов
class Parents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name="Родитель")

    class Meta:
        verbose_name_plural = "Родители студентов"


# Увлечения студентов
class Hobbies(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    hobby = models.CharField(max_length=1000, verbose_name="Увлечение")

    class Meta:
        verbose_name_plural = "Увлечения студентов"


# Преподаватели
class Teacher(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    department = models.CharField(max_length=300, verbose_name='Отделение')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Преподаватели"


# Предметы
class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Дисциплины"


# Успеваемость
class Performance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Преподаватель')
    MARK_CHOICES = [
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('НБ', 'НБ'),
        ('1Н/Б', '1Н/Б')
    ]
    mark = models.CharField(max_length=5, choices=MARK_CHOICES, verbose_name='Оценка')

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name_plural = "Успеваемость"


# Промежуточная аттестация
class AcademicPerformance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Дисциплина')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')
    TYPES_CHOICES = [
        ('Итоговая', 'Итоговая аттестация'),
        ('Промежуточная', 'Промежуточная аттестация'),
    ]
    type_of_perfomance = models.CharField(max_length=15, choices=TYPES_CHOICES, verbose_name='Вид аттестации')
    MARK_CHOICES = [
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('Н/А', 'Н/А'),
        ('Зачёт', 'Зачёт'),
        ('Не зачёт', 'Не зачёт')
    ]
    mark = models.CharField(max_length=8, choices=MARK_CHOICES, verbose_name='Оценка')

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name_plural = "Аттестации"
        unique_together = ['student', 'subject', 'teacher', 'type_of_perfomance', 'mark', ]
