from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'home'

    # Прорисываем метод, импортирующий любые сигналы
    def ready(self):
        import home.signals  # noqa
