from django.forms import ModelForm, widgets
from store.models import Cart


class PopulateCart(ModelForm):
    class Meta:
        model = Cart
        exclude = [ 'id']
        labels = {
            "product": "",
        }
        error_messages = {
            'quantity': {
                'max_length': "This writer's name is too long.",
            },
        }
        widgets = {
            "user":widgets.HiddenInput(),
            'product': widgets.HiddenInput(),
            'quantity': widgets.NumberInput(attrs={'class': 'form-control','min':1,'max': '99','type': 'number'})
        }



