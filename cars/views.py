from django.shortcuts import render
from .models import Car

# Create your views here.
def cars(request):
    cars_data = Car.objects.all()
    
    return render(request, 'pages/cars.html',{'cars_data':cars_data})
