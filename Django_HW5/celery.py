import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_HW5.settings')

app = Celery('Django_HW5')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# # Создаём простейшую функцию, чтобы проверить,
# # что селери работает правильно.
# # Оборачиваем её в декоратор.
# @app.task(bind=True)
# def task_test(self):
#     return 2 + 2
