from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html

from home.models import Student


# Создаём класс, который будет
# отображаться в Django admin
class StudentAdmin(ModelAdmin):
    # Выводим названия колонок в базе данных для отображения в админке.
    list_display = ('name_link_social', 'birthday', 'email')

    # Выводим названия колонок в базе данных для фильтрованияя в таблице админки.
    list_filter = ('name',)

    # Выводим названия колонок в базе данных для поиска в админке.
    search_fields = ('name',)

    # Выводим названия колонок в базе данных для сортировки в таблице админки.
    ordering = ('-name',)

    # Выодим названия колонок в базе данных для изменения в админке.
    fields = ('name', 'surname', 'social_url', 'email', 'birthday',)

    # Создаём метод добавления кастомного поля и ссылки на соцсеть.
    def name_link_social(self, object):
        return format_html("<a href='{}' target='_blank'>{} {}</a>",
                           object.social_url, object.name, object.surname)


# Регистрируем модель "Student" и класс
# "StudentAdmin" в Django admin
admin.site.register(Student, StudentAdmin)
