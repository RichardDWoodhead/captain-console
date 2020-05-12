from django.forms import ModelForm, widgets
from django import forms
from store.models import Cart

class populate_cart(ModelForm):
    class Meta:
        model = Cart
        exclude = [ 'id' ]
        widgets = {
            'user': widgets.NumberInput(attrs={'class': 'form-control'}),
            'product': widgets.NumberInput(attrs={'class': 'form-control'}),
            'quantity': widgets.NumberInput(attrs={'class': 'form-control'})
        }



