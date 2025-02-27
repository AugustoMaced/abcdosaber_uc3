from django.db import models
from titulo.models import Titulo

# Create your models here.
class Instrutor(models.Model):
    """Modeo representando um tipo de Atividade"""
    id = models.AutoField(primary_key=True,
                                 help_text='Id do Instrutor')
    rg= models.CharField(max_length=15, null=False,
                                help_text='Rg do Intrutor')
    nome= models.CharField(max_length=70, null=False,
                           help_text='nome do instrutor')
    dataNascimento = models.DateField(null=True, blank=True,
                                      help_text='data de nascimento do instrutor')
    telefone= models.CharField(max_length=9,
                               help_text='Numero de telefone do instrutor')
    ddd= models.CharField(max_length=9,
                           help_text='informe o ddd do instrutor')
    codigo_titulo = models.ForeignKey(Titulo,null=True,
                                       blank=True, on_delete=models.SET_NULL, db_column="titulo_codigo")
    
    
    def __str__(self):
        return f'{self.id} - {self.nome}'
