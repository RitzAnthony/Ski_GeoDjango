
from django.shortcuts import render, redirect
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
    slopes = Slope.objects.filter(skiresort_id=skiresort_id)
    name = slopes[1].skiresort.name

    ser = serialize('geojson', slopes, geometry_field='geom', fields=('pk', 'name', 'other_tags', 'aerialway', 'status'))
    return render(request, 'details.html', {'skiresorts': ser, 'name': name})

@csrf_exempt
def update_slope_view(request, slope_id):

    slope = Slope.objects.filter(id=slope_id)[0]
    print('before ' + str(slope.status))
    slope.status = not slope.status
    slope.save()
    print('after ' + str(slope.status))
    return redirect('details', skiresort_id=slope.skiresort_id)


def popup_view(request):
    return render(request, 'popup.html')


def resort_popup_view(request, skiresort_id):
    resort = Skiresort.objects.filter(id=skiresort_id)
    return render(request, 'resort_popup.html', {'resort': resort})


