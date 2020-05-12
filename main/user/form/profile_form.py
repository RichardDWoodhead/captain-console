from django.forms import widgets, ModelForm
from user.models import ProfilePicture, Profile
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'user', 'username', 'password', 'search_history']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone_nr': widgets.NumberInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class ImageForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'user', 'username', 'password', 'search_history', 'last_name', 'first_name',
                   'phone', 'email']
        widgets = {
            'profile_pic': widgets.TextInput(attrs={'class': 'form-control'}),
        }
