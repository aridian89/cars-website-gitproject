from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    features_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.order_by('created_date').all()
    feature = {
        'features_cars':features_cars,
        'teams':teams,
        'latest_cars':latest_cars
    }

    return render(request, 'pages/home.html', feature)
def about(request):
    teams = Team.objects.all()
    return render(request, 'pages/about.html',{'teams':teams})
def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
