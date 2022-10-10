from django import forms
from u4uapp.models import Comentario

class NuevoComentarioModelForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
