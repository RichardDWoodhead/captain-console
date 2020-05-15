from django.shortcuts import render, redirect
from contact_us.form.message_form import ContactUs
from contact_us.models import Messages


def contact_us(request):
    if request.method == "POST":
        form = ContactUs(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_us/received.html')
    else:
        return render(request, "contact_us/index.html", {
            'form': ContactUs
        })


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