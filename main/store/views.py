from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from store.Forms.add_to_basket import PopulateCart
from store.Forms.payment_info_form import PaymentInfoForm
from store.Forms.place_order_form import PlaceOrderForm
from store.models import Product, ProductImage, Manufacturer, Cart, Order
from django.http import HttpResponse, JsonResponse


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
    form = PopulateCart(data=data)
    return render(request, "store/product_details.html", context={"product": cproduct[0], 'form': form})


@login_required
def add_to_cart(request):
    data = {"quantity": request.POST["quantity"], "user": request.user, "product":request.POST["product"]}

    if request.method == 'POST':
        form = PopulateCart(data=data or None)
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
        form = PopulateCart()


@login_required
def cart(request):
    cart_items = [{
        "product": Product.objects.get(id=x.product_id).name,
        "user": x.user_id,
        "quantity": x.quantity,
        "image": list(ProductImage.objects.raw("SELECT id from store_productimage WHERE product_id ="+str(x.product_id)+" and main_image"))[0].image
    }for x in Cart.objects.raw("SELECT id from store_cart WHERE user_id ="+str(request.user.id))]
    print(list(ProductImage.objects.raw("SELECT id from store_productimage WHERE product_id ="+str(1)))[0].image)
    return render(request, "store/cart.html", context={"cart_items": cart_items})


@login_required
def payment(request):
    if request.method == "POST":
        data = request.POST.copy()
        data['user'] = request.user.id
        form = PaymentInfoForm(data=data or None)
        if form.is_valid():
            cart_items = [{
                "product": Product.objects.get(id=x.product_id).name,
                "user": x.user_id,
                "quantity": x.quantity,
                "image": list(ProductImage.objects.raw(
                    "SELECT id from store_productimage WHERE product_id =" + str(x.product_id) + " and main_image"))[
                    0].image
            } for x in Cart.objects.raw("SELECT id from store_cart WHERE user_id =" + str(request.user.id))]
            return render(request, "store/checkout/review.html", context={'form': form, 'data': data, 'cart_items': cart_items})
    return render(request, "store/checkout/payment.html", context={'form': PaymentInfoForm})


@login_required
def edit_payment(request):
    if request.method == "POST":
        return render(request, "store/checkout/payment.html", context={'form': PaymentInfoForm(data=request.POST)})


@login_required
def add_payment_info(request):
    if request.method == "POST":
        form = PaymentInfoForm(data=request.POST or None)
        if form.is_valid():
            form.save()
            return product(request, request.POST['product'])


@login_required
def review(request):
    return render(request, "store/checkout/review.html")


@login_required
def confirmation(request):
    if request.method == "POST":
        order_form = PaymentInfoForm(data = request.POST)
        if order_form.is_valid():
            order_form.save()
            cart_items = list(Cart.objects.all().filter(user_id=request.user.id))
            current_order = list(Order.objects.raw('select id from store_order where user_id ='+ str(request.user.id)))[0]
            data = {'order': int(current_order.id)}
            for item in cart_items:
                data['product'] = int(item.product_id)
                data['quantity'] = int(item.quantity)
                current_form = PlaceOrderForm(data=data)
                if current_form.is_valid():
                    current_form.save()
                    item.delete()

        return render(request, "store/checkout/confirmation.html")
