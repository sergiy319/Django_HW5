from django.db import models


# Создаём класс Student. Он будет описывать
# атрибуты к каждому студенту
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.CharField(max_length=200, blank=True, null=True)
    normalized_name = models.CharField(max_length=200, blank=True, null=True)
    normalized_surname = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    social_url = models.URLField(max_length=500, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    subject = models.ForeignKey('home.Subject', on_delete=models.SET_NULL, null=True)


# Создаём класс "Teacher". Он будет
# описывать преподавателей.
class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    # Связываем модель "Teacher" со студентами.
    students = models.ManyToManyField('home.Student')


# Создаём класс "Subject". Он будет описывать
# предметы изучаемые студентами.
class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)


# Создаём класс "Book". Он будет описывать
# зачётки, принадлежащие студентам.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)

    student = models.OneToOneField('home.Student', on_delete=models.CASCADE, null=True)
