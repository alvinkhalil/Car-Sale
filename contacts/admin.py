from contacts.models import Contact, ContactModel
from django.contrib import admin

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ["car_id","first_name","car_title","email","customer_need","created_date"]
    search_fields = ["car_title","message"]
    list_filter = ["created_date","car_title"]

admin.site.register(Contact,ContactAdmin)

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["name",'email',"subject","phone","created_date"]
    list_filter = ["created_date"]
    search_fields = ["name","email","subject"]

admin.site.register(ContactModel,ContactModelAdmin)