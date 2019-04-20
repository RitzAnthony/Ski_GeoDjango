from django.contrib.gis.db import models


class Slope(models.Model):
    name = models.CharField(max_length=200)
    geom = models.MultiPolygonField(srid=21781, null=True)

    class Meta:
        db_table = "slopes"

    def __str__(self):
        return self.name
