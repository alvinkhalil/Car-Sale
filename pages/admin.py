from pages.models import Teams
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

class TeamsAdmin(admin.ModelAdmin):
    def photo_icon(self,object):
        return format_html("<img src = '{}' width = 40 style = 'border-radius: 50px;' />".format(object.photo.url))
    
    photo_icon.short_description = "Şəkil"

    list_display = ["id","photo_icon","first_name","last_name","designation","created_date"]
    search_fields = ["first_name","last_name","destignation"]
    list_filter = ["created_date","designation"]
    list_display_links = ["id","first_name"]

admin.site.register(Teams, TeamsAdmin)