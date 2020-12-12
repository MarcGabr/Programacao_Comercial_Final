from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
logger = logging.getLogger(__name__)

@login_required
def sair(request):
    print('aqui')
    logout(request)
    return render(request, 'registration/login.html')

class Autenticacao(View):
    def get(self, request):
        contexto ={
            'usuario':'',
            'senha': '',
        }
        return render(request, 'registration/login.html', contexto)

    def post(self, request):
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        logger.info('Usuario:{usuario}'.format(usuario=usuario))
        logger.info('Senha: {senha}'.format(senha=senha))

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request,user)
                #return HttpResponse('/veiculos')
            #return render(request,'login.html', {'mensagem':'Usuario inativo'})
            return redirect('/prontoatendimento')

        return render(request,'registration/login.html', {'mensagem':'Usuario não cadastrado ou senha incorreta'})
