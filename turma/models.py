from django.db import models
from instrutor.models import Instrutor
from tipodeatividade.models import TipoDeAtividade
from aluno.models import Aluno

# Create your models here.
class Turma(models.Model):
    """Modeo representando um tipo de Atividade"""
    numero = models.AutoField(primary_key=True,
                                 help_text='Numero da Turma')
    horarioAula= models.TimeField(null=False,
                                help_text='horario da Aula')
    duracaoAula= models.DurationField(null=False,
                           help_text='Duracao da Aula')
    dataInicial = models.DateField(null=False, blank=False,
                                      help_text='data inicial da turma')
    dataFinal= models.DateField(null=True, blank=True,
                               help_text='Data Final da turma ')
    codigoAtividade = models.ForeignKey(TipoDeAtividade,null=True,
                                       blank=True, on_delete=models.SET_NULL, db_column="codigoAtividade")
    matriculaMonitor = models.ForeignKey(Aluno,null=True,
                                       blank=True, on_delete=models.SET_NULL, db_column="matriculaMonitor")
    idIntrutor = models.ForeignKey(Instrutor,null=True,
                                       blank=True, on_delete=models.SET_NULL, db_column="idIntrutor")
    
    
    
    def __str__(self):
        return f'{self.numero} - {self.horarioAula}'
