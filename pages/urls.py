from django.urls import path
from pages import views
from contacts.views import contactme

app_name = "pages"

urlpatterns = [
    path('index',views.home),
    path('',views.home,name = "home"),
    path('about/',views.about,name = "about"),
    path('services/',views.services,name = "services"),
    path('contact/',contactme,name = "contact"),


]


