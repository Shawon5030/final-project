from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(NameForm)
admin.site.register(YoutubeChannel)
admin.site.register(EmailSettings)
admin.site.register(Customer)

@admin.register(AddMoney)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['user' , 'earning' , 'payment']
    
from django.contrib import admin
from .models import SiteSettings

admin.site.register(SiteSettings)