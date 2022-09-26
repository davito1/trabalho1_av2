from django.apps import AppConfig


class TarefaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tarefa'


    def __str__(self):
        return self.nome
