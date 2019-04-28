from django.contrib.gis.db import models
from skiresorts.models import Skiresort

class Slope(models.Model):
    name = models.CharField(max_length=200, null=True)
    geom = models.LineStringField(srid=4326, null=True)
    highway = models.CharField(max_length=200, null=True)
    aerialway = models.CharField(max_length=200, null=True)
    other_tags = models.CharField(max_length=500, null=True)
    status = models.NullBooleanField()
    skiresort = models.ForeignKey(Skiresort, on_delete=models.CASCADE,
                                  null=True,
                                  db_column='fk_skiresort')

    class Meta:
        db_table = "slopes"

    def __str__(self):
        return self.name
