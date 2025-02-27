
from django.db import models
from django.urls import reverse 

# Create your models here.
class Aluno(models.Model):
    """Modelo representando um aluno"""
    matricula = models.AutoField(primary_key=True, 
                                 help_text='Código do Aluno')
    nome = models.CharField(max_length=70, null=False, 
                            help_text='Informe o nome do aluno')
    dataInicial = models.DateField(null=False,blank=False, 
                                   help_text='Data inicial do Aluno')
    dataFinal = models.DateField(null=True,blank=True, 
                                 help_text='Data Final do Aluno')

    def __str__(self):
        return f'{self.matricula} - {self.nome} - {self.dataInicial} - {self.dataFinal}'
