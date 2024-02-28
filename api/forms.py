from django import forms
from .models import Item


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('currency',)
        widgets = {
            'currency': forms.Select(attrs={'class': 'form-control'}),
        }


