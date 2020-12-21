from django.forms import ModelForm
from home.models import Student


# Создаём класс "StudentForm", который наследуется
# от "BaseForm" и отвечает за создание формы на вебе
class StudentForm(ModelForm):
    # Прописываем откаой модели "StudentForm" будет
    # черпать информацию. Для этого создаём "class Meta"
    class Meta:
        model = Student
        # Сохраняем в "fields" взятые из "models.py"
        # поля, которые хотим отобразить
        fields = ['name', 'surname', 'social_url', 'age', 'sex', 'address',
                  'description', 'birthday', 'email'
                  ]
