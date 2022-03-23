from django.shortcuts import render
from .models import  team


# Create your views here.
def home(request):
    teams = team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, "pages/home.html", data)


def cars(request):
    return render(request, "pages/cars.html")


def about(request):
    teams = team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, "pages/about.html", data)


def service(request):
    return render(request, "pages/service.html")


def contact(request):
    return render(request, "pages/contact.html")

def login(request):
    return render(request, "")