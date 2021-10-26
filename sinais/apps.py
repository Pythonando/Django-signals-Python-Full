from django.apps import AppConfig


class SinaisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sinais'

    def ready(self):
        import sinais.signals