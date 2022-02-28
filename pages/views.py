from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    features_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.order_by('created_date').all()
    make = Car.objects.values_list('make',flat=True).distinct()
    model = Car.objects.values_list('model',flat=True).distinct()
    cities = Car.objects.values_list('cities',flat=True).distinct()
    year = Car.objects.values_list('year',flat=True).distinct()
    body_type = Car.objects.values_list('body_type',flat=True).distinct()

    feature = {
        'features_cars':features_cars,
        'teams':teams,
        'latest_cars':latest_cars,
        'make':make,
        'model':model,
        'cities':cities,
        'year':year,
        'body_type':body_type,
    }

    return render(request, 'pages/home.html', feature)
def about(request):
    teams = Team.objects.all()
    return render(request, 'pages/about.html',{'teams':teams})
def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
