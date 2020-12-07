from django.core.management import BaseCommand
from faker import Faker
from home.models import Student


# Файл "insert_student.py" является местом,
# где мы прописываем все команды

# Тело команд составляет класс "Command".
# Command наследуется от "BaseCommand"
class Command(BaseCommand):
    # Вводим атрибут "help", который пояснит при вызове назначение "Command"
    help = 'Insert new students to the system'

    # Инициализируем метод для передачи аргументов
    def add_arguments(self, parser):
        parser.add_arguments('-l', '--len', type=int, default=10)

    # Инициализируем метод для непосредственного хранеия команд
    def handle(self, *args, **options):
        # Инициализируем библиотеку "Faker"
        faker = Faker()

        for _ in range(options['len']):
            student = Student()

            # Присваиваем рандобные значения с помощью
            # библиотеки "Faker"
            student.id = faker.id()
            student.name = faker.name()
            student.surname = faker.surname()
            student.age = faker.age()
            student.sex = faker.sex()
            student.address = faker.address()
            student.description = faker.description()
            student.birthday = faker.birthday()
            student.email = faker.email()

            # Сохраняем значения
            student.save()
