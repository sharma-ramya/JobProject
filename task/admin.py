#from django.contrib import admin

from django.contrib.gis import admin
from .models import Place
from django.contrib.gis.admin import  OSMGeoAdmin
from leaflet.admin import LeafletGeoAdminMixin, LeafletGeoAdmin

# Register your models here.


@admin.register(Place)
class PlaceAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'location')