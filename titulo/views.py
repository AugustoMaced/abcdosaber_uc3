# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<!DOCType html><html><body><p>Olá, estou no App 'Titulos (lembrando que é só um teste)'</p></body></html>")

def nome(request):
    return HttpResponse("Nome feião irmão")