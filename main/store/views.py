from django.shortcuts import render
from django.http import HttpResponse

products = {
    1: {"id": 1, "name": "ps2", "price": 15000, "image": "images/ps2.png"},
    2: {"id": 2, "name": "ps2", "price": 15000, "image": "images/ps2.png"},
    3: {"id": 3, "name": "ps2", "price": 15000, "image": "images/ps2.png"},
    4: {"id": 4, "name": "ps3", "price": 20000, "image": "images/ps3.jpg"},
    5: {"id": 5, "name": "ps3", "price": 20000, "image": "images/ps3.jpg"},
    6: {"id": 6, "name": "ps3", "price": 20000, "image": "images/ps3.jpg"},
    7: {"id": 7, "name": "ps3", "price": 20000, "image": "images/ps3.jpg"},
    8: {"id": 8, "name": "ps3", "price": 20000, "image": "images/ps3.jpg"},
    9: {"id": 9, "name": "ps3", "price": 20000, "image": "images/ps3.jpg"},
    10: {"id": 10, "name": "ps3", "price": 20000, "image": "images/ps3.jpg"},
    11: {"id": 11, "name": "ps4", "price": 35000, "image": "images/ps4.jpg"},
    12: {"id": 12, "name": "ps4", "price": 35000, "image": "images/ps4.jpg"},
    13: {"id": 13, "name": "ps4", "price": 35000, "image": "images/ps4.jpg"},
    14: {"id": 14, "name": "ps4", "price": 35000, "image": "images/ps4.jpg"},
}


# Create your views here.
def index(request):
    return render(request, "store/index.html", context={"products": products.values()})


def product(request, id):
    return render(request, "store/product_details.html", context={"product": products[id]})



