from django.shortcuts import render

products = [
    {"name": "ps2", "price":15000, "image": "images/ps2.png"},
    {"name": "ps3", "price":20000, "image": "images/ps3.jpg"},
    {"name": "ps4", "price":35000, "image": "images/ps4.jpg"},
]


# Create your views here.
def index(request):
    return render(request, "store/index.html", context={"products":products})