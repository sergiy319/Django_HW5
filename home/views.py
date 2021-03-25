import csv

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView

from home.emails import send_email
from home.forms import StudentForm, UserSignUpForm
from home.models import Student


class SignUpView(View):

    def get(self, request):
        sign_up_form = UserSignUpForm()

        return render(request, 'sign_up.html', context={
            'form': sign_up_form,
        })

    def post(self, request):
        sign_up_form = UserSignUpForm(request.POST)
        if sign_up_form.is_valid():
            user = sign_up_form.save()
            user.is_active = False
            user.set_password(request.POST['password1'])
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))

            activate_url = "{}/{}/{}".format(
                "http://localhost:8000/activate",
                uid,
                default_token_generator.make_token(user=user)
            )

            send_email(
                recipient_list=[user.email],
                activate_url=activate_url
            )

            return HttpResponse("Check your email list to activate account!")
        return HttpResponse("Wrong Data")


class ActivateView(View):

    def get(self, request, uid, token):
        user_id = force_bytes(urlsafe_base64_decode(uid))

        user = User.objects.get(pk=user_id)

        if not user.is_active and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()

            login(request, user)

            return HttpResponse('token checked')

        return HttpResponse('Your account activated')


class SignInView(View):

    def get(self, request):
        auth_form = AuthenticationForm()

        return render(request, 'sign_in.html', context={
            'form': auth_form,
        })

    def post(self, request):
        auth_form = AuthenticationForm(request.POST)
        user_a = authenticate(request=request,
                              username=request.POST.get('username'),
                              password=request.POST.get('password'))
        login(request, user_a)

        return redirect('/')


class SignOutView(View):

    def get(self, request):
        logout(request)
        return HttpResponse('Logouted')


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


# Create a new class for generating and
# downloading CSW files.
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
