from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from store.Forms.add_to_basket import populate_cart
from store.Forms.payment_info_form import payment_info_form
from store.models import Product, ProductImage, Manufacturer, Cart

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
    data = {"product": product_id, "user": "1", "quantity": "1"}
    form = populate_cart(data=data)
    return render(request, "store/product_details.html", context={"product": cproduct[0], 'form': form})


@login_required
def add_to_cart(request):
    data = {"quantity": request.POST["quantity"], "user": request.user, "product":request.POST["product"]}

    if request.method == 'POST':
        form = populate_cart(data=data or None)
        if form.is_valid():
            form.save()
            return redirect("product/"+data["product"])

        # print(request.POST)

        # cproduct = [{
        #     'product_id': order_item.id,
        #     'user_id': order_item.user_id,
        #     'quantity': order_item.quantity
        # }]
        # return render(request, "store/product_details.html", context={"product": cproduct[0]})
    else:
        form = populate_cart()


def cart(request):
    cart_items = [{
        "product": Product.objects.get(id=x.product_id).name,
        "user": x.user_id,
        "quantity": x.quantity,
    }for x in Cart.objects.raw("SELECT id from store_cart WHERE user_id ="+str(request.user.id))]
    return render(request, "store/cart.html", context={"cart_items": cart_items})


@login_required
def payment(request):
    return render(request, "store/checkout/payment.html", context={'form': payment_info_form})

def add_payment_info(request):
    if request.method == "POST":
        form = payment_info_form(data=request.POST or None)
        if form.is_valid():
            form.save()
            return product(request, request.POST['product'])


@login_required
def review(request):
    return render(request, "store/checkout/review.html")


@login_required
def confirmation(request):
    return render(request, "store/checkout/confirmation.html")