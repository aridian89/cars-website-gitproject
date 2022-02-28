from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
    cars_data = Car.objects.order_by('-created_date')
    paginator = Paginator(cars_data, 4)
    page = request.GET.get('page')
    paged_car = paginator.get_page(page)
    features_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.order_by('created_date').all()
    make = Car.objects.values_list('make',flat=True).distinct()
    model = Car.objects.values_list('model',flat=True).distinct()
    cities = Car.objects.values_list('cities',flat=True).distinct()
    year = Car.objects.values_list('year',flat=True).distinct()
    body_type = Car.objects.values_list('body_type',flat=True).distinct()


    data = {
        'cars_data':paged_car,
        'make':make,
        'model':model,
        'cities':cities,
        'year':year,
        'body_type':body_type,
    }

    return render(request, 'cars/cars.html',data)
def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car':single_car,
    }
    return render(request, 'cars/car_detail.html',data)

def search(request):
    search_cars_data = Car.objects.all()
    make = Car.objects.values_list('make',flat=True).distinct()
    model = Car.objects.values_list('model',flat=True).distinct()
    cities = Car.objects.values_list('cities',flat=True).distinct()
    year = Car.objects.values_list('year',flat=True).distinct()
    body_type = Car.objects.values_list('body_type',flat=True).distinct()
    transmition = Car.objects.values_list('transmition',flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            search_cars_data = search_cars_data.filter(model__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            search_cars_data = search_cars_data.filter(model__iexact=model)
    if 'make' in request.GET:
        make = request.GET['make']
        if make:
            search_cars_data = search_cars_data.filter(make__iexact=make)
    if 'cities' in request.GET:
        cities = request.GET['cities']
        if cities:
            search_cars_data = search_cars_data.filter(cities__iexact=cities)

    if 'body_type' in request.GET:
        body_type = request.GET['body_type']
        if body_type:
            search_cars_data = search_cars_data.filter(body_type__iexact=body_type)
    if 'transmition' in request.GET:
        transmition = request.GET['transmition']
        if body_type:
            search_cars_data = search_cars_data.filter(transmition__iexact=body_type)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if min_price:
            search_cars_data = search_cars_data.filter(price__gte=min_price,price__lte=max_price)
    data = {
        'search_cars_data':search_cars_data,
        'make':make,
        'transmition':transmition,
        'model':model,
        'cities':cities,
        'year':year,
        'body_type':body_type,
    }

    return render(request,'cars/search.html',data)
