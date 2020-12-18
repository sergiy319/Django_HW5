from django.shortcuts import render, redirect

from home.forms import StudentForm
from home.models import Student


def show_string(request):
    return render(request, 'index.html', context={'name': 'World!'})


def home(request):
    # student = Student()
    # student.save()

    if request.method == 'GET':
        students = Student.objects.all()

        student_form = StudentForm()

        context = {
            'students': students,
            'form': student_form,
        }

        return render(
            request,
            'index.html',
            context=context
        )
    elif request.method == 'POST':

        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student_form.save()

        return redirect('/home')
