from django.contrib import admin
from .models import (Medico,Paciente, Atendimento)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nomedamae', 'profissao')

admin.site.register(Medico)
admin.site.register(Atendimento)
admin.site.register(Paciente,PacienteAdmin)
