from django.shortcuts import render
from .models import team
from cars.models import car


def home(request):
    teams = team.objects.all()
    feature_cars = car.objects.order_by('-created_date').filter(is_feature=True)
    all_cars = car.objects.order_by('-created_date')

    model_search = car.objects.values_list('model', flat=True).distinct()
    city_search = car.objects.values_list('city', flat=True).distinct()
    year_search = car.objects.values_list('year', flat=True).distinct()
    body_style_search = car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'feature_cars': feature_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,

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





def login(request):
    return render(request, "")
