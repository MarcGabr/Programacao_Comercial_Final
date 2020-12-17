from rest_framework import serializers
from .models import Medico, Paciente, Atendimento

class SerializadorMedico(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('id', 'nome', 'numeroregional', 'especializacao')

class SerializadorPaciente(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('id', 'nome', 'cns', 'nomedamae')

class SerializadorAtendimento(serializers.ModelSerializer):
    class Meta:
        model = Atendimento
        exclude = []