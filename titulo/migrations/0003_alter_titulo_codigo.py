# Generated by Django 4.2.18 on 2025-02-11 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titulo', '0002_alter_titulo_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulo',
            name='codigo',
            field=models.AutoField(help_text='Código do tipo de atividade', primary_key=True, serialize=False),
        ),
    ]
