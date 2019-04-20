from django.contrib.gis import admin
from .models import Skiresort

# also register Geo classes
admin.site.register(Skiresort, admin.OSMGeoAdmin)
