from django.shortcuts import render
from django import forms
from store.Forms.add_to_basket import populate_cart
from store.models import Product, ProductImage, Manufacturer


from django.http import HttpResponse, JsonResponse


class SearchForm(forms.Form):
    query = forms.CharField(label='query', max_length=100)


# Create your views here.
def index(request):
    manufacturers = list(Manufacturer.objects.raw("SELECT distinct id FROM store_manufacturer"))
    return render(request, "store/index.html", context={"manufacturers": manufacturers})


def get_products(request):
    products = [{
        'id': x["id"],
        'name': x["name"],
        'description': x["description"],
        'price': x["price"],
        'type': x["type"],
        'image': str(ProductImage.objects.raw("SELECT id from store_productimage WHERE product_id = "+str(x["id"])+" AND main_image")[0].image),
        'manufacturer': str(Manufacturer.objects.raw("SELECT id from store_manufacturer WHERE id = " + str(x["manufacturer_id"]))[0].name),
    } for x in list(Product.objects.values())]
    manufacturers = list(Manufacturer.objects.all().values())
    return JsonResponse({"products": products, "manufacturers": manufacturers})


def product(request, product_id):
    cproduct = [{
        'id': int(x.id),
        'name': x.name,
        'description': x.description,
        'price': x.price,
        'type': x.type,
        'other_images': list(ProductImage.objects.raw("SELECT id from store_productimage WHERE product_id ="+str(product_id)+" AND NOT main_image")),
        'main_image': str(ProductImage.objects.raw("SELECT id from store_productimage WHERE product_id = "+str(x.id)+" AND main_image")[0].image),
        'manufacturer': str(Manufacturer.objects.raw("SELECT id from store_manufacturer WHERE id = " + str(x.manufacturer_id))[0].name),

    } for x in list(Product.objects.raw("SELECT id from store_product WHERE id ="+str(product_id)))]
    form = populate_cart()
    return render(request, "store/product_details.html", context={"product": cproduct[0], 'form': form})

def add_to_cart(request):
    if request.method == 'POST':
        print(request.POST)
        form = populate_cart(data = request.POST or None)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return product(request,request.POST['product'])

        # print(request.POST)

        # cproduct = [{
        #     'product_id': order_item.id,
        #     'user_id': order_item.user_id,
        #     'quantity': order_item.quantity
        # }]
        # return render(request, "store/product_details.html", context={"product": cproduct[0]})
    else:
        form = populate_cart()


def payment(request):
    return render(request, "store/checkout/pay.html")


def review(request):
    return render(request, "store/checkout/review.html")


def confirmation(request):
    return render(request, "store/checkout/confirmation.html")