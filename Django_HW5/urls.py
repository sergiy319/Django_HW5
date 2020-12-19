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

from home.views import home as home_view, update_student, HomeView, UpdateStudentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', home_view, name='students'),
    path('students/class/', HomeView.as_view(), name='students_class'),
    path('student/update/<id>/', update_student, name='update_students'),
    path('student/update/class/<id>/', UpdateStudentView.as_view(), name='update_students_class'),
]
