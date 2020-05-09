from django.shortcuts import render
from django import forms
from store.models import Product
from user.models import User

from django.http import HttpResponse, JsonResponse


class SearchForm(forms.Form):
    query = forms.CharField(label='query', max_length=100)


# Create your views here.
def index(request):
    return render(request, "store/index.html")


def get_products(request):
    data = list(Product.objects.values())
    return JsonResponse({"data": data})


def product(request, product_id):
    return render(request, "store/product_details.html", context={"product": products[product_id]})


def payment(request):
    return render(request, "store/checkout/pay.html")


def review(request):
    return render(request, "store/checkout/review.html")


def confirmation(request):
    return render(request, "store/checkout/confirmation.html")