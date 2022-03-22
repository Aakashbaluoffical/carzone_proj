from django.shortcuts import render
from . import views


# Create your views here.
def home(request):
    return render(request, "pages/home.html")


def cars(request):
    return render(request, "pages/cars.html")


def about(request):
    return render(request, "pages/about.html")


def service(request):
    return render(request, "pages/service.html")


def contact(request):
    return render(request, "pages/contact.html")

def login(request):
    return render(request, "")