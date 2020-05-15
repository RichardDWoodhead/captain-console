from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.forms import SimpleArrayField, forms
from django.forms import widgets, ModelForm
from user.models import ProfilePicture, Profile
from user.models import User


class ProfileForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'user', 'search_history']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class SearchHistoryForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'user', 'first_name', 'last_name', 'phone_number', 'email', 'profile_pic']
        fields = {
            'search_history': ArrayField(forms.CharField(max_length=9999))
        }


class ImageForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'user', 'search_history', 'last_name', 'first_name',
                   'phone', 'email']
        widgets = {
            'profile_pic': widgets.TextInput(attrs={'class': 'form-control'}),
        }


