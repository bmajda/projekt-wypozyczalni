from django import forms
from .models import Awaria

class AwariaForm(forms.ModelForm):
    class Meta:
        model = Awaria
        fields = ['opis_usterki']
        labels = {
            'opis_usterki': 'Opisz co się zepsuło',
        }
        widgets = {
            'opis_usterki': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }