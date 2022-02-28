from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
    cars_data = Car.objects.order_by('-created_date')
    paginator = Paginator(cars_data, 4)
    page = request.GET.get('page')
    paged_car = paginator.get_page(page)

    data = {
        'cars_data':paged_car,
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
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            search_cars_data = search_cars_data.filter(model__icontains=keyword)
    data = {
        'search_cars_data':search_cars_data,
    }
    return render(request,'cars/search.html',data)
