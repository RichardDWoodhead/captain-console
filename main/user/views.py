from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from store.models import Product, ProductImage
from user.form.profile_form import ImageForm
from user.form.profile_form import ProfileForm
from user.models import Profile
from user.models import User
import django.contrib.auth.models


def user(request):
    return render(request, "user/index.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


@login_required
def profile(request):
    profile = User.objects.filter(user=request.user).first()
    if profile == None:
        return redirect('edit_profile')
    return render(request, 'user/profile.html', {
        'profile': profile
    })



@login_required
def edit_profile(request):
    profile = User.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/edit_profile.html', {
        'form': ProfileForm(instance=profile)
    })


def history(request):
    items = [{
        'product_id': str(i.id),
        'product_name': i.name,
        'product_image': str(ProductImage.objects.raw("SELECT id from store_productimage WHERE product_id = "+str(i.id)+" AND main_image")[0].image),
    } for i in list(Product.objects.all())]
    profile = User.objects.filter(user=request.user).first()
    product_history = profile.search_history
    items_ids = [d['product_id'] for d in items]
    products = []
    if product_history != None:
        for i in product_history:
            products.append(items[items_ids.index(i)])
        return render(request, 'user/history.html', context={'products': products})
    else:
        return redirect('store_index')