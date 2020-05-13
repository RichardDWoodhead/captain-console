from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.form.profile_form import ImageForm
from user.form.profile_form import ProfileForm
from user.models import Profile


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
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })


@login_required
def edit_profile_pic(request):
    profile = user.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ImageForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        return render(request, 'user/edit_profile_pic.html', {
            'form': ImageForm(instance=profile)
        })


