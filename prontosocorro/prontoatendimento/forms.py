from django.forms import ModelForm
from .models import Medico, Paciente, Atendimento

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        exclude = []
        fields = '__all__'

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        exclude = []
        fields = '__all__'

class AtendimentoForm(ModelForm):
    class Meta:
        model = Atendimento
        exclude = []
        fields = '__all__'