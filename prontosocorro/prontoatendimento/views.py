from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import (Paciente, Medico, Atendimento)
from .forms import PacienteForm, MedicoForm, AtendimentoForm
#from prontosocorro.utilitarios import AutenticacaoObrigatoria
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def index(request):
    pacientes = Paciente.objects.all()[:10]
    medicos = Medico.objects.all()[:10]
    atendimento = Atendimento.objects.all()[:10]
    Qtdpacientes = Paciente.objects.all().count()
    Qtdmedicos = Medico.objects.all().count()
    Qtdatendimento = Atendimento.objects.all().count()

    data = {'pacientes': pacientes,
            'medicos': medicos,
            'atendimentos': atendimento,
            'Qtdpaciente': Qtdpacientes,
            'Qtdmedicos': Qtdmedicos,
            'Qtdatendimentos': Qtdatendimento,
            }
    return render(request, 'prontoatendimento/index.html', data)

@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    data = {'pacientes': pacientes}
    return render(request, 'prontoatendimento/paciente_listar.html', data)

@login_required
def novo_paciente(request):
    if request.method == 'POST':
        formpaciente = PacienteForm(request.POST or None)

        if formpaciente.is_valid():
            formpaciente.save()
        return redirect('listar-pacientes')
    else:
        form = PacienteForm()
        data = {'form': form}
        return render(request, 'prontoatendimento/paciente_novo.html', data)

@login_required
def update_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    print(form)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar-pacientes')
    else:
        data = {}
        data['paciente'] = paciente
        data['form'] = form
        return render(request, 'prontoatendimento/paciente_update.html', data)

@login_required
def delete_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    # if request.method == 'POST':
    paciente.delete()
    return redirect('listar-pacientes')
    # else:
    # return render(request, 'core/delete_pessoa.html', {'pessoa': pessoa})

@login_required
def lista_medicos(request):
    medicos = Medico.objects.all()
    data = {'medicos': medicos}
    return render(request, 'prontoatendimento/medico_listar.html', data)

@login_required
def novo_medico(request):
    if request.method == 'POST':
        formmedico = MedicoForm(request.POST or None)
        if formmedico.is_valid():
            formmedico.save()
        return redirect('listar-medicos')
    else:
        form = MedicoForm()
        data = {'form': form}
        return render(request, 'prontoatendimento/medico_novo.html', data)

@login_required
def update_medico(request, id):
    medico = Medico.objects.get(id=id)
    form = MedicoForm(request.POST or None, instance=medico)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('listar-medicos')
    else:
        data = {}
        data['medico'] = medico
        data['form'] = form
        return render(request, 'prontoatendimento/medico_update.html', data)

@login_required
def delete_medico(request, id):
    medico = Medico.objects.get(id=id)
    medico.delete()
    return redirect('listar-medicos')

@login_required
def lista_atendimentos(request):
    atendimentos = Atendimento.objects.all()
    data = {'atendimentos': atendimentos}
    return render(request, 'prontoatendimento/atendimento_listar.html', data)

@login_required
def novo_atendimento(request):
    if request.method == 'POST':
        formatendimento = AtendimentoForm(request.POST or None)
        print(formatendimento)
        if formatendimento.is_valid():
            formatendimento.save()
        return redirect('listar-atendimentos')
    else:
        form = AtendimentoForm()
        data = {'form': form}
        return render(request, 'prontoatendimento/atendimento_novo.html', data)

@login_required
def update_atendimento(request, id):
    atendimento = Atendimento.objects.get(id=id)
    form = AtendimentoForm(request.POST or None, instance=atendimento)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar-atendimentos')
    else:
        data = {}
        data['atendimento'] = atendimento
        data['form'] = form
        return render(request, 'prontoatendimento/atendimento_update.html', data)

@login_required
def delete_atendimento(request, id):
    atendimento = Atendimento.objects.get(id=id)
    atendimento.delete()
    return redirect('listar-atendimentos')

@login_required
def busca(request):
    pacientes = list(Paciente.objects.all().values('nome', 'cpf', 'datanasc', 'Telefone','sexo','nomedamae','cns','id'))
    medicos = list(Medico.objects.all().values('nome', 'cpf', 'sexo',  'cbo', 'numeroregional', 'especializacao','id'))
    data = {'pacientes': pacientes, 'medicos': medicos}
    return JsonResponse(data, safe=False)
