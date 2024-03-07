from django.db import models

# Create your models here.

class Jugador(models.Model):

    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Nickname = models.CharField(max_length=30)
    Email = models.EmailField()

    def __str__(self):
        return self.Nickname

class Juez(models.Model):

    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Edad = models.IntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.Nombre

class Categoria(models.Model):

    NombreCategoria = models.CharField(max_length=30)
    Juego = models.CharField(max_length=30)
    Temporada = models.IntegerField()

    def __str__(self):
        return self.NombreCategoria

    