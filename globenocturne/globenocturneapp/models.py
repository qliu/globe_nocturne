from django.contrib.gis.db import models

class SatYear(models.Model):
    year = models.IntegerField(primary_key=True)
    
    def __unicode__(self):
            return str(self.year)
    
    class Meta:
        verbose_name = 'Year'
        db_table = u'sat_year'
        
class Satellite(models.Model):
#    id  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Satellite'
        db_table = u'satellite'

class DMSPProduct(models.Model):
#    id  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'DMSP Product'
        db_table = u'dmsp_product'
        
class DMSPDataset(models.Model):
#    id  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,null='True',blank='True')
    year = models.ForeignKey('SatYear',verbose_name='Year')
    satellite = models.ForeignKey('Satellite',verbose_name='Satellite')
    product = models.ForeignKey('DMSPProduct',verbose_name='DMSP Product')
    wms_layer = models.CharField(max_length=100,verbose_name='WMS Layer')
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):       
        # auto generate name based on selection
        self.name = "%s-%s-%s" % (str(self.year),self.satellite.name,self.product.name)
        super(DMSPDataset, self).save(*args, **kwargs)
        
    def previous(self):
        try:
            previous_records = DMSPDataset.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return DMSPDataset.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = DMSPDataset.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return DMSPDataset.objects.get(id=next_id)
        except:
            return None    
    
    class Meta:
        verbose_name = 'DMSP Dataset'
        db_table = u'dmsp_dataset'


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