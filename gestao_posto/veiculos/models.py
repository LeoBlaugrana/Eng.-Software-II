# app_veiculos/models.py
from django.db import models

class Veiculo(models.Model):
    nome = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()

    def __str__(self):
        return self.nome
