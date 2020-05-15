from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    path('', LoginView.as_view(template_name='user/index.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/',  views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile')
]