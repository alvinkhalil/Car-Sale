from django.http.response import HttpResponse
from pages.models import Teams
from django.shortcuts import render
from cars.models import Car
# Create your views here.
def home(request):
    teams = Teams.objects.all()
    featured_cars = Car.objects.order_by("-created_date").filter(is_featured = True)
    latest_cars = Car.objects.order_by("-created_date").all()
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city', flat=True).distinct()
    year_fields = Car.objects.values_list('year', flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style', flat=True).distinct()



    context = {
        "teams":teams,
        "featured_cars":featured_cars,
        "latest_cars":latest_cars,
        "model_fields":model_fields,
        "city_fields":city_fields,
        "year_fields":year_fields,
        "body_style_fields":body_style_fields,

        
    }
    return render(request, "pages/index.html",context)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, "pages/services.html")

def search(request):

    cars = Car.objects.order_by("-created_date")
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city', flat=True).distinct()
    year_fields = Car.objects.values_list('year', flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style', flat=True).distinct()


    if "keyword" in request.GET:

        keyword = request.GET.get("keyword")

        if keyword:
                cars = cars.filter(description__icontains = keyword)
            

    if "model" in request.GET:

        keyword = request.GET.get("model")

        if keyword:
                cars = cars.filter(model__icontains = keyword)

    if "year" in request.GET:

        keyword = request.GET.get("year")

        if keyword:
                cars = cars.filter(year__icontains = keyword)

    if "city" in request.GET:

        keyword = request.GET.get("city")

        if keyword:
                cars = cars.filter(city__icontains = keyword)

    if "body_style" in request.GET:

        keyword = request.GET.get("body_style")

        if keyword:
                cars = cars.filter(body_style__icontains = keyword)
                        
    if "min_price" in request.GET:

        max_price = request.GET.get("max_price")
        min_price = request.GET.get("min_price")


        if max_price:
                cars = cars.filter(price__gte = min_price, price__lte = max_price )

    context = {
        "cars":cars,
        "model_fields":model_fields,
        "city_fields":city_fields,
        "year_fields":year_fields,
        "body_style_fields":body_style_fields,
    }
    return render(request,"pages/search.html",context)