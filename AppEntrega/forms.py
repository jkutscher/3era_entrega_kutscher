from django import forms

class JugadorFormulario(forms.Form):

    Nombre = forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)
    Nickname = forms.CharField(max_length=30)
    Email = forms.EmailField()

class JuezFormulario(forms.Form):

    Nombre = forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)
    Edad = forms.IntegerField()
    Email = forms.EmailField()

class CategoriaFormulario(forms.Form):

    NombreCategoria = forms.CharField(max_length=30)
    Juego = forms.CharField(max_length=30)
    Temporada = forms.IntegerField()
