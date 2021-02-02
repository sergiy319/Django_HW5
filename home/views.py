import csv
from time import sleep

from django.conf import settings
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from home.emails import send_email
from home.forms import StudentForm
from home.models import Student


def show_string(request):
    return render(request, 'index.html', context={'name': 'World!'})


def home(request, *args, **kwargs):
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

        return redirect(reverse('students'))


# Создаём функцию для изменения характеристик студентов.
def update_student(request, id):
    if request.method == 'GET':

        # Выбираем студента через ID
        student = Student.objects.get(id=id)

        # Создаём формочку для заполнения характеристик студента.
        student_form = StudentForm(instance=student)

        # Передаём в "context" форму и ID
        context = {
            'form': student_form,
            'id': student.id,
        }

        return render(
            request,
            'update.html',
            context=context,
        )
    elif request.method == 'POST':

        # Выбираем студента по ID
        student = Student.objects.get(id=id)

        # В форму заносим "POST" изменённые данные и имя студента
        student_form = StudentForm(request.POST, instance=student)

        # Проверяем на валидность и сохраняем изменения
        if student_form.is_valid():
            student_form.save()

            # Меняем хардкод url на "reverse()"
            return redirect(reverse('students'))

        else:
            return HttpResponseBadRequest('apparent client error')


# Создаём "endpoint" который будет принимать данные из формы
# для того чтобы изменить информацию о конкретном студенте.
class UpdateStudentView(View):

    def get_student(self, id):

        try:
            self.student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            self.student = None
        except Student.MultipleObjectsReturned:
            self.student = None

    def get(self, request, id, *args, **kwargs):
        print(kwargs)

        self.get_student(id)

        student_form = StudentForm(instance=self.student)

        context = {
            'form': student_form,
            'id': self.student.id,
        }

        return render(
            request,
            'update.html',
            context=context,
        )

    def post(self, request, id):

        self.get_student(id)

        student_form = StudentForm(request.POST, instance=self.student)

        if student_form.is_valid():
            student_form.save()

            return redirect(reverse('students'))

        else:
            return HttpResponseBadRequest('apparent client error')


# Creates a decorator for class caching.
@method_decorator(cache_page(settings.CACHE_TTL), name='dispatch')
# Create an "endpoint" for displaying student
# forms and data in them that we can change.
class HomeView(View):
    def get(self, request):
        sleep(10)
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

    def post(self, request):
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student_form.save()

        return redirect(reverse('students'))


# Create a new class for generating and
# downloading FSW files.
class CSVView(View):
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        # Create an expression in which the file
        # is available only for download.
        response['Content-Disposition'] = "attachment; filename=data_students.csv"
        # Create a response wrapper for writing data.
        writer_for_response = csv.writer(response)
        # The first line is the column information line.
        writer_for_response.writerow(["Name", "Book", "Subject"])

        students = Student.objects.all()

        for student in students:
            # The rest of the columns are written
            # as the body of the CSV file.
            writer_for_response.writerow([
                student.name,
                student.book.title if student.book else None,
                student.subject.title if student.subject else None,
            ])

        return response


# Create a new class to display student data
# in JSON format.
class JsonView(View):
    def get(self, request):
        # Taking a list of students.
        students = Student.objects.all()

        return JsonResponse({
            # Converting values through model
            # instances to dictionaries.
            "students": list(students.values(
                "name",
                "book__title",
                "subject__title",
            )),
        })


class SendMailView(View):
    def get(self, request):
        # Define a list of email recipients.
        send_email(recipient_list=['1414sergiy@gmail.com', '319naumovs@gmail.com'])

        return HttpResponse('Email sent!')


class StudentsView(ListView):
    model = Student
    template_name = 'students.html'
