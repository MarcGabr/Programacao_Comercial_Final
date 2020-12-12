from django.conf.urls import url, re_path
from django.urls import path, include
from prontosocorro.views import sair
from .views import (index, lista_pacientes, novo_paciente,update_paciente, delete_paciente, lista_medicos,
novo_medico, update_medico, delete_medico, lista_atendimentos, novo_atendimento, update_atendimento, delete_atendimento, busca)

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^listar-pacientes',lista_pacientes , name='listar-pacientes'),
    url(r'^novo-paciente',novo_paciente, name='novo-paciente'),
    re_path(r'^update-paciente/(?P<id>\d+)/$', update_paciente, name='update-paciente'),
    re_path(r'^delete-paciente/(?P<id>\d+)/$', delete_paciente, name='delete-paciente'),
    url(r'^listar-medicos', lista_medicos, name='listar-medicos'),
    url(r'^novo-medico', novo_medico, name='novo-medico'),
    re_path(r'^update-medico/(?P<id>\d+)/$', update_medico, name='update-medico'),
    re_path(r'^delete-medico/(?P<id>\d+)/$', delete_medico, name='delete-medico'),
    url(r'^listar-atendimentos', lista_atendimentos, name='listar-atendimentos'),
    url(r'^novo-atendimento', novo_atendimento, name='novo-atendimento'),
    re_path(r'^update-atendimento/(?P<id>\d+)/$', update_atendimento, name='update-atendimento'),
    re_path(r'^delete-atendimento/(?P<id>\d+)/$', delete_atendimento, name='delete-atendimento'),
    path('busca', busca, name='busca'),
]