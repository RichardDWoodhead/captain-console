from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]