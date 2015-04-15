from django.contrib.gis.db import models

class WorldBorder(models.Model):
    gid = models.IntegerField(primary_key=True)
    iso = models.CharField(max_length=2)
    country = models.CharField(max_length=50)
    countryaff = models.CharField(max_length=50)
    affiso = models.CharField(max_length=2)
    geom = models.MultiPolygonField(srid=3857)
    objects = models.GeoManager()
    
    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'World Border'
        db_table = u'worldborder'