from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_entity'

    def ready(self):
        import user_entity.signals  # Import the signals module explicitly