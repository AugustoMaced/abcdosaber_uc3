# Generated by Django 4.2.18 on 2025-02-06 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('codigo', models.IntegerField(help_text='Código do tipo de atividade', primary_key=True, serialize=False)),
                ('descricao', models.CharField(help_text='Informe a descrição do tipo de atividade', max_length=70)),
            ],
        ),
    ]
