from django.urls import path, include
from . import views

urlpatterns = [
    
    path('nome/', views.nome, name='nome'),

]

