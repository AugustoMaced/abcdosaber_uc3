from django.db import models
from django.urls import reverse 


# Create your models here.
class Titulo(models.Model):
    """Modeo representando um tipo de Atividade"""
    codigo = models.AutoField(primary_key=True,
                                 help_text='Código do tipo de atividade')
    descricao= models.CharField(max_length=70, null=False,
                                help_text='Informe a descrição do tipo dO TITULO')
    
    def __str__(self):
        return f'{self.codigo} - {self.descricao}'
