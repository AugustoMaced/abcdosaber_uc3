# Generated by Django 4.2.18 on 2025-02-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulo',
            name='descricao',
            field=models.CharField(help_text='Informe a descrição do tipo dO TITULO', max_length=70),
        ),
    ]
