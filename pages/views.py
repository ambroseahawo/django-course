from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 148937,
        "my_list": [834, 19, 28, 'ABC']
    }
    return render(request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
