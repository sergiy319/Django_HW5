from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from home.models import Student


# Create a class "StudentForm", which is inherited
# from "BaseForm" and is responsible for creating
# a form on the web.
class StudentForm(ModelForm):
    # Prescribe the "StudentForm" model to take the
    # information. To do this, create a "class Meta".
    class Meta:
        model = Student
        # Save in "fields" the fields that we want
        # to display taken from "models.py".
        fields = ['name', 'surname', 'social_url', 'age', 'sex', 'address',
                  'description', 'birthday', 'email', 'picture'
                  ]


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
