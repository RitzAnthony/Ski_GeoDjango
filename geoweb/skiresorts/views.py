
from django.shortcuts import render
from .models import Skiresort
from django.core.serializers import serialize
from shapely.geometry import MultiPolygon
from shapely import wkt
from slopes.models import Slope




def index(request):
    '''
    canton_of_valais = Canton.objects.filter(name='Valais')[0]
    valaisShape = wkt.loads(canton_of_valais.geom.wkt).convex_hull

    skiresorts = Skiresort.objects.all()

    result = []

    for resort in skiresorts:
        resortShape = wkt.loads(resort.geom.wkt).convex_hull
        if valaisShape.contains(resortShape):
            result.append(resort)


    ser = serialize('geojson', result, geometry_field='geom', fields=('name',))

    for val in result:
        print(val.geom.wkt)
    '''

    slopes = Slope.objects.filter(skiresort__name__icontains='saint luc')

    ser = serialize('geojson', slopes, geometry_field='geom', fields=('name', 'other_tags', 'aerialway'))
    return render(request, 'index.html', {'skiresorts': ser})


def slope_update_view(request):
    print(request.POST)
    slope = request.POST.get('slope')

    slopes = Slope.objects.filter(skiresort__name__icontains='saint luc')

    ser = serialize('geojson', slopes, geometry_field='geom', fields=('name', 'other_tags', 'aerialway'))

    return render(request, 'index.html', {'skiresorts': ser})
