from django.shortcuts import render
from .models import team
from cars.models import car


def home(request):
    teams = team.objects.all()
    feature_cars = car.objects.order_by('-created_date').filter(is_feature=True)
    all_cars = car.objects.order_by('-created_date')
    data = {
        'teams': teams,
        'feature_cars': feature_cars,
        'all_cars': all_cars,
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