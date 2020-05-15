from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render, redirect
from django import forms
from store.Forms.add_to_basket import PopulateCart
from store.Forms.payment_info_form import PaymentInfoForm
from store.Forms.place_order_form import PlaceOrderForm
from store.models import Product, ProductImage, Manufacturer, Cart, Order
from django.http import HttpResponse, JsonResponse
import user.models


# Create your views here.
from user.form.profile_form import SearchHistoryForm, ProfileForm


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
    if not isinstance(request.user, AnonymousUser):
        profile = user.models.User.objects.filter(user=request.user).first()
        if profile == None:
            form = ProfileForm(instance=profile, data=request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile = profile.save()
        profile = user.models.User.objects.filter(user=request.user).first()
        print(profile.search_history)
        if profile.search_history == None:
            history = [product_id]
        else:
            history = list(profile.search_history)
            history.append(str(product_id))
            history = list(set(history))
        form = SearchHistoryForm(instance=profile, data={'search_history': history})
        if form.is_valid():
            form.save()
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
    if request.method == 'POST':

        data = {"quantity": request.POST["quantity"], "user": request.user, "product":request.POST["product"]}
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
    else:
        return redirect("store_index")


@login_required
def clear_cart(request):
    if request.method == "POST":
        try:
            cart_items = Cart.objects.raw("SELECT id from store_cart WHERE user_id ="+str(request.user.id))
            for item in cart_items:
                item.delete()
            return redirect("cart")
        except:
            return redirect("cart")
    return redirect("cart")


@login_required
def cart(request):
    cart_items = [{
        "product": Product.objects.get(id=x.product_id).name,
        "price": int(Product.objects.get(id=x.product_id).price.replace(".", "")),
        "user": x.user_id,
        "quantity": x.quantity,
        "image": list(ProductImage.objects.raw("SELECT id from store_productimage WHERE product_id ="+str(x.product_id)+" and main_image"))[0].image
    }for x in Cart.objects.raw("SELECT id from store_cart WHERE user_id ="+str(request.user.id))]
    total = 0
    for i in range(len(cart_items)):
        total += int(cart_items[i]["price"])
    return render(request, "store/cart.html", context={"cart_items": cart_items, "total": total})


@login_required
def payment(request):
    if request.method == "POST":
        data = request.POST.copy()
        data['user'] = request.user.id
        form = PaymentInfoForm(data=data or None)
        if form.is_valid():
            cart_items = [{
                "product": Product.objects.get(id=x.product_id).name,
                "price": int(Product.objects.get(id=x.product_id).price.replace(".", "")),
                "user": x.user_id,
                "quantity": x.quantity,
                "image": list(ProductImage.objects.raw(
                    "SELECT id from store_productimage WHERE product_id =" + str(x.product_id) + " and main_image"))[
                    0].image
            } for x in Cart.objects.raw("SELECT id from store_cart WHERE user_id =" + str(request.user.id))]
            total = 0
            for i in range(len(cart_items)):
                total += int(cart_items[i]["price"])
            return render(request, "store/checkout/review.html", context={'form': form, 'data': data, 'cart_items': cart_items, "total": total})
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
