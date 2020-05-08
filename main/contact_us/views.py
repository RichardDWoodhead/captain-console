from django.shortcuts import render
from django import forms
from django.http import HttpResponse


# Create your views here.


def contact_us(request):
    return render(request, "contact_us/index.html")


'''
def search(request):
    filtered_list = []
    form = SearchForm(request.GET)
    if form.is_valid():
        search_string = form.cleaned_data["query"]
        for i in products.values():
            if search_string in i["name"]:
                filtered_list.append(i)
    return render(request, "store/index.html", context={"products": filtered_list})'''