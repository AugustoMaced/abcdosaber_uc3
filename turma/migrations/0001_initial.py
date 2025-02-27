# Generated by Django 4.2.18 on 2025-02-13 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipodeatividade', '0003_alter_tipodeatividade_codigo'),
        ('instrutor', '0001_initial'),
        ('aluno', '0002_alter_aluno_datafinal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('numero', models.AutoField(help_text='Numero da Turma', primary_key=True, serialize=False)),
                ('horarioAula', models.TimeField(help_text='horario da Aula')),
                ('duracaoAula', models.DurationField(help_text='Duracao da Aula')),
                ('dataInicial', models.DateField(help_text='data inicial da turma')),
                ('dataFinal', models.DateField(blank=True, help_text='Data Final da turma ', null=True)),
                ('codigoAtividade', models.ForeignKey(blank=True, db_column='codigoAtividade', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tipodeatividade.tipodeatividade')),
                ('idIntrutor', models.ForeignKey(blank=True, db_column='idIntrutor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='instrutor.instrutor')),
                ('matriculaMonitor', models.ForeignKey(blank=True, db_column='matriculaMonitor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='aluno.aluno')),
            ],
        ),
    ]
