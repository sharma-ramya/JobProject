from django.shortcuts import render

from django.views import generic # django generic view

from django.contrib.gis.geos import fromstr, Point #to get our longitude and latitude

from django.contrib.gis.db.models.functions import Distance #to calculate distance

from .models import Place #import our model

from django.http import HttpResponse

from django.core.serializers import serialize

from django.contrib.gis.serializers import geojson

long = 77.12
lat = 28.38

my_location = Point(long, lat, srid=4326)

class Home(generic.ListView):
    model = Place
    context_object_name = 'places'
    queryset = Place.objects.annotate(distance=Distance('location', my_location)).order_by('distance')[0:6]
    template_name = 'home.html'


#places_datasets : this uses the serializer to convert the data “Myplaces.objects.all()” to “geojson” data
#to use it for the leaflet map.
def places_dataset(request):

    place = serialize('geojson', Place.objects.all())
    return HttpResponse(place, content_type='json')