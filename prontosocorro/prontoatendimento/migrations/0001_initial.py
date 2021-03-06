# Generated by Django 3.1.2 on 2020-11-25 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('datanasc', models.DateTimeField(blank=True, null=True)),
                ('Telefone', models.CharField(max_length=20)),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhuma das opções')], max_length=1)),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='prontoatendimento.pessoa')),
                ('especializacao', models.CharField(max_length=100)),
                ('numeroregional', models.CharField(max_length=10)),
                ('cbo', models.CharField(max_length=10)),
            ],
            bases=('prontoatendimento.pessoa',),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='prontoatendimento.pessoa')),
                ('nomedamae', models.CharField(max_length=100)),
                ('profissao', models.CharField(max_length=50)),
                ('cns', models.CharField(max_length=15)),
            ],
            bases=('prontoatendimento.pessoa',),
        ),
    ]
