from django.shortcuts import render
from django import forms
from store.models import Product, ProductImage


from django.http import HttpResponse, JsonResponse


class SearchForm(forms.Form):
    query = forms.CharField(label='query', max_length=100)


# Create your views here.
def index(request):
    return render(request, "store/index.html")


def get_products(request):
    products = [{
        'id': x["id"],
        'name': x["name"],
        'description': x["description"],
        'price': x["price"],
        'image': str(ProductImage.objects.raw("SELECT id from store_productimage WHERE product_id = "+str(x["id"])+" AND mainimage")[0].image),
    } for x in list(Product.objects.values())]
    return JsonResponse({"products": products})


def product(request, product_id):
    cproduct = [{
        'id': x.id,
        'name': x.name,
        'description': x.description,
        'price': x.price,
        'other_images': list(ProductImage.objects.raw("SELECT id from store_productimage WHERE product_id ="+str(product_id)+" AND NOT mainimage")),
        'main_image': str(ProductImage.objects.raw("SELECT id from store_productimage WHERE product_id = "+str(x.id)+" AND mainimage")[0].image),
    } for x in list(Product.objects.raw("SELECT id from store_product WHERE id ="+str(product_id)))]
    print(cproduct[0]["other_images"])
    return render(request, "store/product_details.html", context={"product": cproduct[0]})


def payment(request):
    return render(request, "store/checkout/pay.html")


def review(request):
    return render(request, "store/checkout/review.html")


def confirmation(request):
    return render(request, "store/checkout/confirmation.html")