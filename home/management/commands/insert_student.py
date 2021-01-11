import uuid

from django.core.management import BaseCommand
from faker import Faker
from home.models import Student, Subject, Book, Teacher


# Файл "insert_student.py" является местом,
# где мы прописываем команды.

# Тело команд составляет класс "Command".
# Command наследуется от "BaseCommand".
class Command(BaseCommand):
    # Вводим атрибут "help", который пояснит при вызове назначение "Command".
    help = 'Insert new students to the system'

    # Инициализируем метод для передачи аргументов.
    def add_arguments(self, parser):
        parser.add_argument('-l', '--len', type=int, default=10)

    # Инициализируем метод для непосредственного хранеия команд.
    def handle(self, *args, **options):
        # Инициализируем библиотеку "Faker".
        faker = Faker()

        for _ in range(options['len']):
            subject, _ = Subject.objects.get_or_create(title='Python')
            subject.save()

            book = Book()
            book.title = uuid.uuid4()
            book.save()

            # student = Student()

            # # Присваиваем рандомные значения с помощью
            # # библиотеки "Faker".
            # student.name = faker.name()
            # student.surname = faker.last_name()
            # student.age = faker.random_int(min=18, max=53)
            # student.sex = faker.simple_profile()['sex']
            # student.address = faker.address()
            # student.description = faker.text()
            # student.birthday = faker.simple_profile()['birthdate']
            # student.email = faker.email()
            # student.subject = subject
            #
            # # Сохраняем значения
            # student.save()

            teacher, _ = Teacher.objects.get_or_create(name='Fedor')
            teacher.save()

            # Выбираем с помощью фильтра только женский пол.
            female_students = Student.objects.filter(sex='F')

            # Создаём связь между таблицами.
            teacher.students.add(*female_students)

    # Инициализируем метод для удаления студента из базы.
    def delete_some_student(self):
        # Создаём переменную для выбора по "id".
        some_student = Student.objects.first()
        return some_student.delete()
