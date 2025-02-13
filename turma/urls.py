from django.urls import path, include
from . import views

urlpatterns = [
    
    path('informacao/', views.informacao, name='informacao'),

]

