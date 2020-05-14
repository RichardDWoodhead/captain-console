from django.forms import ModelForm, widgets
from store.models import ProductOrder

class place_order_form(ModelForm):
    class Meta:
        model = ProductOrder
        exclude = ['id']
        widgets = {
            'quantity': widgets.NumberInput(),
            'order_id': widgets.NumberInput(),
            'product_id': widgets.NumberInput()
        }


