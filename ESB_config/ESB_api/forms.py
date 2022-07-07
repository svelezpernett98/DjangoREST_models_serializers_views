from django import forms


class formulario_json(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    telefono = forms.CharField()


