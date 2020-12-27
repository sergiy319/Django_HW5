import logging

from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin


# Создаём "MIDDLEWARE" для отслеживание логов.
class LogMiddleware(MiddlewareMixin):

    def process_view(self, request, view_funk, view_args, view_kwargs):
        # Функцию "resolve()" применяем для вытягивания
        # информации по пути в запросе.
        resolved_path_info = resolve(request.path_info)

        # Если страница - это отображение студентов,
        # передадим доп. параметр во "view".
        if resolved_path_info.url_name == 'students_list':
            some_variable = 3
            return view_funk(request, some_variable)

        # Остальных будем отображать как обычно.
        return view_funk(request, *view_args, **view_kwargs)


# Создаём "MIDDLEWARE" для отслеживания "request".
class RawDataMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # Функцию "resolve()" применяем для вытягивания
        # информации по пути в запросе.
        resolved_path_info = resolve(request.path_info)

        # Функцию "Logging()" применяем для ведения лога.
        logging.info('Request %s View name %s route %s', request,
                     resolved_path_info.view_name, resolved_path_info.route)


# Создаём "MIDDLEWARE" для отслеживания "response".
class IdentifyResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        # Функцию "Logging()" применяем для ведения лога.
        logging.info('For request %s response %s', request, response)

        return response
