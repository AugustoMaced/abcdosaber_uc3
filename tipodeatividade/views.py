from django.shortcuts import render
from django.http import HttpResponse

from tipodeatividade.models import TipoDeAtividade

# Create your views here.
def index(request):
    return HttpResponse("<!DOCType html><html><body><p>Olá, estou no App 'Tipo de Atividade'</p></body></html>")

def listar(request):
    lista_tiposdeatividade= TipoDeAtividade.objects.order_by("-descricao")
    resposta = "<ul>"
    for tipodeatividade in lista_tiposdeatividade:
        resposta += '<li>{0}</li>'.format(tipodeatividade.descricao)

    resposta += '</ul>'
    print(resposta)
    return HttpResponse(resposta)

    
def show_mensagem(request):
    x = "A"
    nome = x + "ugusto, tudo bem ?"
    return HttpResponse(f"Bom dia ! {nome}")

def detalhe_tipodeatividade(request, ta_codigo):
    tipodeatividade = TipoDeAtividade.objects.get(pk=ta_codigo)
    return HttpResponse(tipodeatividade)