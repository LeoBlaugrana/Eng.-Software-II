from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from abastecimentos.models import Historico
from veiculos.models import Veiculo
from clientes.models import Motorista
from django.http import JsonResponse

@login_required
def dashboard(request):
    # Coletar dados de cada app
    veiculos = Veiculo.objects.all()
    motoristas = Motorista.objects.all()
    historico = Historico.objects.all()
    
    context = {
        'veiculos': veiculos,
        'motoristas': motoristas,
        'historico': historico,
    }
    return render(request, 'registration/dashboard.html', context)

@login_required
def add_veiculo(request):
    if request.method == 'POST':
        ano = request.POST['ano']
        placa = request.POST['placa']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        motorista_id = request.POST['motorista']
        motorista = Motorista.objects.get(id=motorista_id)
        veiculo = Veiculo(ano=ano, placa=placa, marca=marca, modelo=modelo, motorista=motorista)
        veiculo.save()
        return JsonResponse({
            'success': True,
            'veiculo': {
                'id': veiculo.id,
                'ano': veiculo.ano,
                'placa': veiculo.placa,
                'marca': veiculo.marca,
                'modelo': veiculo.modelo,
                'motorista': veiculo.motorista.nome,
            }
        })
    return JsonResponse({'success': False})

@login_required
def add_motorista(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        motorista = Motorista(nome=nome)
        motorista.save()
        return JsonResponse({
            'success': True,
            'motorista': {
                'id': motorista.id,
                'nome': motorista.nome,
            }
        })
    return JsonResponse({'success': False})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Sua conta foi criada! Você já pode fazer login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


