from django.shortcuts import render

from swissgeo.models import Canton
from .models import Skiresort
from django.core.serializers import serialize
from shapely.geometry import MultiPolygon



def index(request):
    canton_of_valais = Canton.objects.filter(name='Valais')[0]


    skiresorts = Skiresort.objects.filter(geom__contains=canton_of_valais.geom)

    ser = serialize('geojson', skiresorts, geometry_field='geom', fields=('name',))

    for val in skiresorts:
        print(val.geom.wkt)

    return render(request, 'index.html', {'skiresorts': ser})
