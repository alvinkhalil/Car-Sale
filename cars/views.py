from cars.models import Car
from django.core.paginator import Paginator

from django.shortcuts import render

# Create your views here.

def cars(request):

    cars = Car.objects.all()
    paginator = Paginator(cars,2)
    
    page_number = request.GET.get('page')
    page_obj =paginator.get_page(page_number) 

    latest_cars = Car.objects.order_by("-created_date").all()
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city', flat=True).distinct()
    year_fields = Car.objects.values_list('year', flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style', flat=True).distinct()


       
    context = {
        "cars":page_obj,
        "latest_cars":latest_cars,
        "model_fields":model_fields,
        "city_fields":city_fields,
        "year_fields":year_fields,
        "body_style_fields":body_style_fields,
    }

    return render(request, 'cars/cars.html',context)

def car_detail(request,id):

    car_detail = Car.objects.get(id = id)

    context = {
        "car_detail":car_detail,
    }

    return render(request, "cars/car_detail.html",context)