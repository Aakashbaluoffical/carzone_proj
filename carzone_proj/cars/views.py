from django.shortcuts import render, get_object_or_404
from .models import car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def cars(request):
    cars = car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    page_cars = paginator.get_page(page)

    model_search = car.objects.values_list('model', flat=True).distinct()
    city_search = car.objects.values_list('city', flat=True).distinct()
    year_search = car.objects.values_list('year', flat=True).distinct()
    body_style_search = car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'cars': page_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car = get_object_or_404(car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, "cars/car_detail.html", data)


def search(request):
    all_cars = car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            all_cars = all_cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            all_cars = all_cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            all_cars = all_cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            all_cars = all_cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            all_cars = all_cars.filter(body_style__iexact=body_style)
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if 'max_price':
            all_cars = all_cars.filter(price__gte=min_price, price__lte=max_price)

    model_search = car.objects.values_list('model', flat=True).distinct()
    city_search = car.objects.values_list('city', flat=True).distinct()
    year_search = car.objects.values_list('year', flat=True).distinct()
    body_style_search = car.objects.values_list('body_style', flat=True).distinct()

    data = {
        "all_cars": all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,

    }
    return render(request, 'cars/search.html', data)
