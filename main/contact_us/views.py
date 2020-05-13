from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from contact_us.form.message_form import ContactUs
from contact_us.models import Messages


def contact_us(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(user_id=request.user.id)
        except user != None:
            form = ContactUs(data=request.POST)
            if form.is_valid():
                message = Messages()
                message.name = request.POST['name']
                message.phone_number = request.POST['phone_number']
                message.email = request.POST['email']
                message.message = request.POST['message']
                message.save()
                return redirect('contact_us')
            else:
                form = ContactUs(data=request.POST)
                if form.is_valid():
                    message = Messages()
                    message.name = request.POST['name']
                    message.phone_number = request.POST['phone_number']
                    message.email = request.POST['email']
                    message.message = request.POST['message']
                    message.save()
                    return redirect('contact_us')
    else:
        try:
            user = User.objects.get(user_id=request.user.id)
        except:
            user = None
        if user != None:
            return render(request, "contact_us/index.html", {
                'UserData': user.profilepicture,
                'form': ContactUs
            })
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