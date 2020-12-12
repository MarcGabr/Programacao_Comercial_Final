from django.db import models

class Pessoa(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Outros")
    )

    nome = models.CharField(max_length=200, null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True, null=False, blank=False)
    email = models.CharField(max_length=200, null=True, blank=True)
    datanasc = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    Telefone = models.CharField(max_length=20, null=False, blank=False) 
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)


class Paciente(Pessoa):
    nomedamae = models.CharField(max_length=100, null=False, blank=False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    cns = models.CharField(max_length=15, null=False, blank=False)
    #pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.nome, self.cpf, self.email, self.sexo, self.cns)

class Medico(Pessoa):
    especializacao = models.CharField(max_length=100, null=False, blank=False)
    numeroregional = models.CharField(max_length=10, null=False, blank=False)
    cbo = models.CharField(max_length=10, null=False, blank=False)
    #pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.nome, self.cpf, self.email, self.sexo, self.cbo)

class Atendimento(models.Model):
    PROCEDIMENTO_CHOICES = (
        (1, "Consulta"),
        (2, "Retorno"),
        (3, "Enfermaria")
    )

    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, blank=True)

    procedimento = models.IntegerField(choices=PROCEDIMENTO_CHOICES, null=False, blank=False)
    medicacao = models.CharField(max_length=200, null=True, blank=True)
    receitas = models.CharField(max_length=200, null=True, blank=True)
    exames = models.CharField(max_length=200, null=True, blank=True)
    queixa = models.CharField(max_length=200, null=True, blank=True)
    doencas = models.CharField(max_length=200, null=True, blank=True)
    hipotese = models.CharField(max_length=200, null=True, blank=True)
    diagnostico = models.CharField(max_length=200, null=True, blank=True)
    observacoes = models.CharField(max_length=200, null=True, blank=True)
    data_atendimento = models.DateField(null=False)
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.procedimento, self.medico.nome, self.paciente.nome, self.data_atendimento)
