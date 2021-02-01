import re

from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
import gender_guesser.detector as gender

from home.models import Student


# Создаём функцию сигнала для приведения имени к нужному
# стандарту. Оборачиваем её в декоратор "@receiver".
@receiver(pre_save, sender=Student)
def pre_name_required_standard(sender, instance, **kwargs):  # noqa
    # Удаляем спец-символы и приводим имя к нижнему регистру.
    instance.normalized_name = re.sub('[^\w\s]|_', '', instance.name).lower()


# Создаём функцию сигнала для приведения фамилии к нужному
# стандарту. Оборачиваем её в декоратор "@receiver".
@receiver(pre_save, sender=Student)
def pre_surname_required_standard(sender, instance, **kwargs):  # noqa
    # Удаляем спец-символы и приводим фамилию к нижнему регистру.
    instance.normalized_surname = re.sub('[^\w\s]|_', '', instance.surname).lower()


# Создаём функцию сигнала которая будет проверять по "name" пол
# студента и заполнять необходимое поле в таблице(если оно пустое).
# Оборачиваем функцию в декоратор "@receiver".
@receiver(pre_save, sender=Student)
def pre_gender_check(sender, instance, **kwargs):  # noqa
    # С помощью библиотеки "gender_guesser" определяем предположительный пол
    # студента только по имени. Сохраняем эту информацию в колонку "sex".
    gender_check = gender.Detector()
    instance.sex = gender_check.get_gender(instance.name)


# Создаём функцию сигнала перед удалением.
# Оборачиваем функцию в декоратор "@receiver".
# студента "is_active = True" на "is_active = False", и отменять удаление.
# @receiver(pre_delete, sender=Student)
# def pre_delete_check(sender, instance, **kwargs):  # noqa
#     # Действия перед удалением в этой версии не производим.
#     # Вызываем ошибку удаления студента.
#     raise Exception('do not delete')
