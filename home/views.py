from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

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

    def get(self, request, id):

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

    def post(self, request):

        self.get_student(id)

        student_form = StudentForm(request.POST, instance=self.student)

        if student_form.is_valid():
            student_form.save()

            return redirect(reverse('students'))

        else:
            return HttpResponseBadRequest('apparent client error')


# Создаём "endpoint" для отображения формочки студента
# и данными в них которые мы можем изменить.
class HomeView(View):

    def get(self, request):
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
