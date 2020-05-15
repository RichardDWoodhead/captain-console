from django.forms import ModelForm, widgets
from store.models import ProductOrder


class PlaceOrderForm(ModelForm):
    class Meta:
        model = ProductOrder
        exclude = ['id']
        widgets = {
            'quantity': widgets.NumberInput(attrs={'min': 1}),
            'order_id': widgets.NumberInput(attrs={'min': 1}),
            'product_id': widgets.NumberInput(attrs={'min': 1})
        }


