from django.forms import ModelForm, widgets
from django import forms
from store.models import Order


class payment_info_form(ModelForm):
    class Meta:
        model = Order
        exclude = ['id']
        widgets = {
            'date': widgets.TextInput(attrs={'class': 'form-control'}),
            'cardholder_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
        }