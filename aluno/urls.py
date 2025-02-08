from django.urls import path
from . import views

urlpatterns = [
    path('idade/', views.idade, name='idade'),

]
