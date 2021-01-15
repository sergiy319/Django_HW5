from django.db import models


# We create a class "Student".
# It will describe the attributes to each student.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
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


# Create a class "Teacher".
# It will describe the teachers.
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    # Linking the Teacher model to the students.
    students = models.ManyToManyField('home.Student')


# Create the "Subject" class.
# It will describe the subjects studied by the students.
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)


# Create a class "Book".
# It will describe the grade books owned by the students.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)

    student = models.OneToOneField('home.Student', on_delete=models.CASCADE, null=True)


# Create class "Currency".
# It will store exchange rates.
class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    ccy = models.CharField(max_length=10)
    base_ccy = models.CharField(max_length=10)
    buy = models.FloatField()
    sale = models.FloatField()
