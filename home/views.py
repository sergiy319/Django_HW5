from django.shortcuts import render
from home.models import Student


def show_string(request):
    return render(request, 'index.html', context={'name': 'World!'})


def home(request):
    student = Student()
    student.save()

    students = Student.objects.all()

    return render(request, 'index.html', context={'students': students})
