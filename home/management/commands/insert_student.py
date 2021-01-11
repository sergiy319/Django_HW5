import uuid

from django.core.management import BaseCommand
from faker import Faker
from home.models import Student, Subject, Book, Teacher


# The "insert_student.py" file is
# where we write the commands.

# The body of the commands is the "Command" class.
# Command inherits from BaseCommand.
class Command(BaseCommand):
    # Introduce the "help" attribute, which will explain
    # the "Command" assignment when called.
    help = 'Insert new students to the system'

    # Initialize the method for passing arguments.
    def add_arguments(self, parser):
        parser.add_argument('-l', '--len', type=int, default=10)

    # Initialize the method for direct storage of commands.
    def handle(self, *args, **options):
        # Initialize the "Faker" library.
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
            # # Save values.
            # student.save()

            teacher, _ = Teacher.objects.get_or_create(name='Fedor')
            teacher.save()

            # Select only the female gender using the filter.
            female_students = Student.objects.filter(sex='F')

            # We create a link between tables.
            teacher.students.add(*female_students)

    # Initialize the method for removing a student from the database.
    def delete_some_student(self):
        # Create a variable for selection by "id".
        some_student = Student.objects.first()
        return some_student.delete()
