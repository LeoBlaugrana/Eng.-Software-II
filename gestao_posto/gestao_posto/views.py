from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from abastecimentos.models import Historico
from veiculos.models import Veiculo
from clientes.models import Motorista

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


