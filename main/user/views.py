from django.shortcuts import render
from django.http import HttpResponse


def user(request):
    return render(request, "user/index.html")