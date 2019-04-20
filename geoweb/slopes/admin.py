from django.contrib.gis import admin
from .models import Slope

# also register Geo classes
admin.site.register(Slope, admin.OSMGeoAdmin)
