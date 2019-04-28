
from django.shortcuts import render
from .models import Skiresort
from django.core.serializers import serialize
from shapely.geometry import MultiPolygon
from shapely import wkt
from slopes.models import Slope
from django.views.decorators.csrf import csrf_exempt




def resorts_view(request):
    resorts = Skiresort.objects.filter(enabled=True)

    ser = serialize('geojson', resorts, geometry_field='geom', fields=('pk', 'name'))
    return render(request, 'resorts.html', {'resorts': ser})


def details_view(request, skiresort_id):
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

    slopes = Slope.objects.filter(skiresort_id=skiresort_id, other_tags__contains='piste')

    ser = serialize('geojson', slopes, geometry_field='geom', fields=('name', 'other_tags', 'aerialway'))
    return render(request, 'details.html', {'skiresorts': ser})

@csrf_exempt
def update_slope_view(request):
    print('teeeeeessst')

    return render(request, 'resorts.html')


def popup_view(request):
    return render(request, 'popup.html', {})


def resort_popup_view(request, skiresort_id):
    resort = Skiresort.objects.filter(id=skiresort_id)
    return render(request, 'resort_popup.html', {'resort': resort})


