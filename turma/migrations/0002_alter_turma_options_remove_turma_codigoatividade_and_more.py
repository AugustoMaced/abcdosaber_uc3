# Generated by Django 4.2.18 on 2025-02-17 23:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_alter_aluno_datafinal'),
        ('instrutor', '0001_initial'),
        ('tipodeatividade', '0003_alter_tipodeatividade_codigo'),
        ('turma', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turma',
            options={'ordering': ['numero']},
        ),
        migrations.RemoveField(
            model_name='turma',
            name='codigoAtividade',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='dataFinal',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='dataInicial',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='duracaoAula',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='horarioAula',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='idIntrutor',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='matriculaMonitor',
        ),
        migrations.AddField(
            model_name='turma',
            name='codigo_atividade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tipodeatividade.tipodeatividade'),
        ),
        migrations.AddField(
            model_name='turma',
            name='data_final',
            field=models.DateField(blank=True, help_text='Informe a data final da Turma', null=True),
        ),
        migrations.AddField(
            model_name='turma',
            name='data_inicial',
            field=models.DateField(default=datetime.datetime(2025, 2, 17, 23, 11, 42, 509323, tzinfo=datetime.timezone.utc), help_text='Informe a data inicial da Turma'),
        ),
        migrations.AddField(
            model_name='turma',
            name='duracao_aula',
            field=models.SmallIntegerField(default=30, help_text='Informe a duração da aula da Turma'),
        ),
        migrations.AddField(
            model_name='turma',
            name='horario_aula',
            field=models.TimeField(default=datetime.datetime(2025, 2, 17, 23, 11, 42, 509323, tzinfo=datetime.timezone.utc), help_text='Informe a hora em que a hora da aula da Turma'),
        ),
        migrations.AddField(
            model_name='turma',
            name='id_instrutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instrutor.instrutor'),
        ),
        migrations.AddField(
            model_name='turma',
            name='matricula_monitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aluno.aluno'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='numero',
            field=models.AutoField(help_text='Informe a turma do Aluno', primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='TurmaAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio_matricula', models.DateField(default=datetime.datetime(2025, 2, 17, 23, 11, 42, 509323, tzinfo=datetime.timezone.utc), help_text='Data da matrícula do aluno na turma')),
                ('data_fim_matricula', models.DateField(blank=True, help_text='Data de fim de matrícula do aluno na turma', null=True)),
                ('matricula_aluno', models.ForeignKey(help_text='Matrícula do aluno da turma', on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('numero_turma', models.ForeignKey(help_text='Número da turma do aluno.', on_delete=django.db.models.deletion.CASCADE, to='turma.turma')),
            ],
        ),
        migrations.CreateModel(
            name='Ausencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ausencia', models.DateField(default=datetime.datetime(2025, 2, 17, 23, 11, 42, 519330, tzinfo=datetime.timezone.utc), help_text='Data da falta do aluno na turma')),
                ('matricula_aluno', models.ForeignKey(help_text='Matrícula do aluno da turma', on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('numero_turma', models.ForeignKey(help_text='Número da turma do aluno.', on_delete=django.db.models.deletion.CASCADE, to='turma.turma')),
            ],
        ),
    ]
