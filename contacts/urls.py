from django.urls import path
from contacts import views
app_name = "contacts"

urlpatterns = [
    path("inquiry",views.inquiry,name="inquiry"),
    path('',views.contactme,name='contact')



]


