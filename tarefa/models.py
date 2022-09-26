from django.db import models

class Tarefa(models.Model):
    nome_tarefa = models.CharField(max_length=50)
    tipo_tarefa = models.CharField(max_length=200)