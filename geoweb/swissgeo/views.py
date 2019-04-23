from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.core.serializers import serialize

from .models import City, Canton

# Create your views here.


def index(request):
    return HttpResponse("Hi there this is Switzerland")

def city(request,city_id):
    try: 
        city=City.objects.get(pk=city_id)
    except City.DoesNotExist:
        raise Http404("City not found!!")
    #city=get_object_or_404(City,pk=city_id)
    return render(request,'swissgeo/city.html',{'city':city})

def cities(request):
    top_cities=City.objects.order_by('-city_name')[:3]
    template= loader.get_template('swissgeo/index.html')
    context = {
        'top_cities':top_cities,
    }
    #return render(request,'swissgeo/index.html',context)
    return HttpResponse(template.render(context,request))
    #output = ', '.join([c.city_name for c in top_cities])
    #return HttpResponse(output)
    
def canton(request,canton_name):
    
    cantons=Canton.objects.filter(name=canton_name)
    return render(request,'swissgeo/canton.html',{'canton_parts':cantons})

#    return HttpResponse(cantons[1].geom.wkt)

def cantons(request):
    context ={  }
    return render(request, 'swissgeo/cantons.html', context)

def cantonsdata(request):
    cantons=Canton.objects.all()
    ser=serialize('geojson', cantons, geometry_field='geom', fields=('name',))
    
    return HttpResponse(ser)
