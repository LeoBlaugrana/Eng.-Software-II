from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Veiculo, Motorista, Historico

@login_required
def dashboard(request):
    veiculos = Veiculo.objects.all()
    motoristas = Motorista.objects.all()
    historico = Historico.objects.all()
    context = {
        'veiculos': veiculos,
        'motoristas': motoristas,
        'historico': historico,
    }
    return render(request, 'registration/dashboard.html', context)