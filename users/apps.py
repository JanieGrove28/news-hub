from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
<<<<<<< HEAD
        pass
=======
        from .signals import create_groups
        create_groups()
>>>>>>> bf8953c5044d80824794e9511acb31e28f75b7b6
