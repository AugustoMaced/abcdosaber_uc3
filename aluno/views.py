
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def idade(request):
    return HttpResponse("Tu tá velho hein")
    
