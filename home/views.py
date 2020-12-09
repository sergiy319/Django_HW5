from django.shortcuts import render

from home.forms import StudentForm
from home.models import Student


def show_string(request):
    return render(request, 'index.html', context={'name': 'World!'})


def home(request):
    student = Student()
    student.save()

    students = Student.objects.all()

    # Инициализируем "student_form"
    student_form = StudentForm()

    context = {
        'students': students,
        'form': student_form,
    }

    return render(request, 'index.html', context=context)
