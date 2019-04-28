from django.contrib.gis.db import models


class Skiresort(models.Model):
    name = models.CharField(max_length=200)
    geom = models.MultiPolygonField(srid=21781, null=True)
    enabled = models.NullBooleanField()

    class Meta:
        db_table = "skiresorts"

    def __str__(self):
        return self.name
