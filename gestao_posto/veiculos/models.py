# app_veiculos/models.py
from django.db import models
from clientes.models import Motorista

class Veiculo(models.Model):
    ano = models.IntegerField()
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE, null=True, blank=True)  # Permitir nulos temporariamente

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"
