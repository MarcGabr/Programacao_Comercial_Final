# Generated by Django 3.1.2 on 2020-11-26 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prontoatendimento', '0002_auto_20201125_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='medico',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='prontoatendimento.medico'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='paciente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='prontoatendimento.paciente'),
        ),
    ]