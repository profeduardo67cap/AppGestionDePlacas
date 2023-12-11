from django.forms import ModelForm
from .models import Oficina

class OficinaForm(ModelForm):
    class Meta:
        model = Oficina
        fields = ['nombre', 'ciudad', 'telefono','responsable','cp']