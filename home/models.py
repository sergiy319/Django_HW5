from django.db import models


# Создаём класс Student. Он будет описывать
# атрибуты к каждому студенту
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
