from django.shortcuts import render
from django.http import HttpResponse


def user(request):
    return render(request, "user/index.html")
def login(request):
    return render(request, "user/login.html")
def register(request):
    return render(request, "user/register.html")