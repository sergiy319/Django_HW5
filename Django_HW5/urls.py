"""HomeWork_5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home.views import (ActivateView, CSVView, HomeView, JsonView,
                        SendMailView, SignInView, SignOutView, SignUpView,
                        StudentsView, UpdateStudentView)
from home.views import home as home_view
from home.views import update_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', home_view, name='students'),
    path('students/class/', HomeView.as_view(), name='students_class'),
    path('student/update/<id>/', update_student, name='update_students'),
    path('class/student/update/<id>/', UpdateStudentView.as_view(),
         name='update_students_class'),
    path('csv_view', CSVView.as_view(), name='csv_view'),
    path('json_view', JsonView.as_view(), name='json_view'),
    path('send_email/', SendMailView.as_view(), name='send_email'),
    path('students_list', StudentsView.as_view(), name='students_list'),
    path('sign_up', SignUpView.as_view(), name='sign_up_view'),
    path('sign_out', SignOutView.as_view(), name='sign_out_view'),
    path('login', SignInView.as_view(), name='login_view'),
    path('activate/<uid>/<token>', ActivateView.as_view(),
         name='activate_view'),
]
