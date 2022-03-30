from django.shortcuts import render, get_object_or_404
from .models import car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
    cars = car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    page_cars = paginator.get_page(page)
    data = {
        'cars': page_cars,
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car = get_object_or_404(car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, "cars/car_detail.html", data)
