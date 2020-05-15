from django.forms import ModelForm, widgets
from contact_us.models import Messages


class ContactUs(ModelForm):
    class Meta:
        model = Messages
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'message': widgets.Textarea(attrs={'class': 'form-control', 'id': 'comment', 'placeholder': 'Your Message'})
        }