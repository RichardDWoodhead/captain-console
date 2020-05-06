from django.shortcuts import render

products = [
    {"name": "ps2", "price":15000},
    {"name": "ps3", "price":20000},
    {"name": "ps4", "price":35000},
]


# Create your views here.
def index(request):
    return render(request, "store/index.html", context={"products":products})