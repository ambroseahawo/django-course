from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def home_view(*args, **kwargs):
    # return HttpResponse("<h1> Hello world</h1>") # html string
    return render(request, "home.html", {})


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact page</h1>") # html string
