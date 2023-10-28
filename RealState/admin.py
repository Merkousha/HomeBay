from django.contrib import admin
from  RealState.models import Country,State,City,Area ,Property , Property_Images ,Builder



class PropertyImagesInline(admin.TabularInline):
    model = Property_Images
    extra = 10

class PropertyModelADmin(admin.ModelAdmin):
    inlines= [PropertyImagesInline]


# Register your models here.

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Builder)
admin.site.register(Property , PropertyModelADmin)
admin.site.register(Property_Images)
