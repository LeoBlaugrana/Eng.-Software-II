# app_abastecimentos/models.py
from django.db import models
from veiculos.models import Veiculo
from clientes.models import Motorista

class Historico(models.Model):
    data = models.DateField()
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    litros = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.data} - {self.veiculo} - {self.motorista} - {self.litros}L - R${self.valor}"