from django.urls import path
from AppEntrega.views import *

urlpatterns = [
    path('categoria/', crear_categoria, name="Categoria"),
    path('jugador/', crear_jugador, name="Jugador"),
    path('juez/', crear_juez, name="Juez"),
    path('', inicio, name="Inicio"),
    path('buscar_jugador/', buscar_jugador, name='buscar_jugador'),
    path('resultado_jugador/', resultado_jugador, name='resultado_jugador'),
]