from django.db import models


# Создаём новый класс Student
# Он будет описывать дополнительные атрибуты
# к каждому студенту
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField()
    birthday = models.DateField()
    email = models.EmailField(max_length=254)
