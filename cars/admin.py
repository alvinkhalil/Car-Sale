from cars.models import Car
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def photo_icon(self,object):
        
        return format_html("<img src = '{}' width = '40' style = 'border-radius:50px;' />".format(object.car_photo.url))

    list_display = ["id","photo_icon","car_title","color","year","engine","fuel_type","city","transmission","is_featured","created_date"]
    list_display_links = ["id","car_title"]
    list_editable = ["is_featured"]
    list_filter = ["created_date","year","model"]
    search_fields = ["car_title","model","description"]

admin.site.register(Car,CarAdmin)
