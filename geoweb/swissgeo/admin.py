from django.contrib import admin
from django.contrib.gis import admin

# Register your models here.

from .models import City, Hospital, Canton

# register model classes
admin.site.register(City)
admin.site.register(Hospital)

# also register Geo classes
#admin.site.register(Canton, admin.GeoModelAdmin)
admin.site.register(Canton, admin.OSMGeoAdmin)