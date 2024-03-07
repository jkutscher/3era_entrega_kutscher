from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega.models import *
from .models import *
from .forms import *

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")

def crear_jugador(request):

    if request.method == "POST":

        formulario = JugadorFormulario(request.POST)

        if formulario.is_valid():
            info_dicc = formulario.cleaned_data

            nuevo_jugador = Jugador(Nombre = info_dicc["Nombre"],
                                    Apellido = info_dicc["Apellido"],
                                    Nickname = info_dicc["Nickname"],
                                    Email = info_dicc["Email"])
            
            nuevo_jugador.save()

            return render(request, "inicio.html")
    
    else:

        formulario = JugadorFormulario()

    return render(request, "jugador.html", {"form": formulario})

def crear_categoria(request):

    if request.method == "POST":

        formulario = CategoriaFormulario(request.POST)

        if formulario.is_valid():
            info_dicc = formulario.cleaned_data

            nueva_categoria = Categoria(NombreCategoria = info_dicc["NombreCategoria"],
                                    Juego = info_dicc["Juego"],
                                    Temporada = info_dicc["Temporada"],)
            
            nueva_categoria.save()

            return render(request, 'inicio.html')
    
    else:

        formulario = CategoriaFormulario()

    return render(request, "categoria.html", {"form": formulario})

def crear_juez(request):

    if request.method == "POST":

        formulario = JuezFormulario(request.POST)

        if formulario.is_valid():
            info_dicc = formulario.cleaned_data

            nuevo_juez = Juez(Nombre = info_dicc["Nombre"],
                                    Apellido = info_dicc["Apellido"],
                                    Edad = info_dicc["Edad"],
                                    Email = info_dicc["Email"],
                                    )
            
            nuevo_juez.save()

            return render(request, 'inicio.html')
    
    else:

        formulario = JuezFormulario()

    return render(request, "juez.html", {"form": formulario})


def buscar_jugador(request):

    return render(request, "buscar_jugador.html")

def resultado_jugador(request):

    jugador = request.GET.get("Nickname", "")

    resultados = Jugador.objects.filter(Nickname__iexact=jugador)
    
    return render(request, "resultado_jugador.html", {"resultados": resultados})
