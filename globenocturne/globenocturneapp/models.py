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
#    gid = models.IntegerField(primary_key=True)
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

class WorldCountry(models.Model):
#    id = models.IntegerField(primary_key=True)
    fips = models.CharField(max_length=2,null=True,blank=True)
    iso = models.CharField(max_length=2,null=True,blank=True)
    iso3digit = models.CharField(max_length=3,null=True,blank=True)
    name = models.CharField(max_length=250,null=True,blank=True)
    capital = models.CharField(max_length=250,null=True,blank=True)
    continent = models.CharField(max_length=250,null=True,blank=True)
#    area_km = models.FloatField(null=True,blank=True)
    
    def __unicode__(self):
        return self.fips
    
    def previous(self):
        try:
            previous_records = WorldCountry.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return WorldCountry.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = WorldCountry.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return WorldCountry.objects.get(id=next_id)
        except:
            return None    
    
    class Meta:
        verbose_name = 'World Country'
        db_table = u'world_countries'
        
class WorldPoulation(models.Model):
#    id = models.IntegerField(primary_key=True)
    country = models.ForeignKey('WorldCountry')
    year = models.IntegerField(null=True,blank=True)
    value = models.FloatField(null=True,blank=True)
    
    def previous(self):
        try:
            previous_records = WorldPoulation.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return WorldPoulation.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = WorldPoulation.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return WorldPoulation.objects.get(id=next_id)
        except:
            return None    
    
    class Meta:
        verbose_name = 'World Poulation'
        db_table = u'world_population'
        
class WorldGDP(models.Model):
#    id = models.IntegerField(primary_key=True)
    country = models.ForeignKey('WorldCountry')
    year = models.IntegerField(null=True,blank=True)
    value = models.FloatField(null=True,blank=True)
    
    def __unicode__(self):
        return str(self.value)
    
    def previous(self):
        try:
            previous_records = WorldGDP.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return WorldGDP.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = WorldGDP.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return WorldGDP.objects.get(id=next_id)
        except:
            return None    
    
    class Meta:
        verbose_name = 'World GDP'
        db_table = u'world_gdp'


class WorldSOL(models.Model):
#    id = models.IntegerField(primary_key=True)
    country = models.ForeignKey('WorldCountry')
    year = models.IntegerField(null=True,blank=True)
    value = models.FloatField(null=True,blank=True)
    
    def __unicode__(self):
        return str(self.value)
        
    def previous(self):
        try:
            previous_records = WorldSOL.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return WorldSOL.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = WorldSOL.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return WorldSOL.objects.get(id=next_id)
        except:
            return None    
    
    class Meta:
        verbose_name = 'World Sum of Lights'
        db_table = u'world_sol'

class WorldOriginalSOL(models.Model):
    #    id = models.IntegerField(primary_key=True)
    country = models.ForeignKey('WorldCountry')
    year = models.IntegerField(null=True,blank=True)
    sat = models.CharField(max_length=3)    
    sol = models.FloatField(null=True,blank=True)
    dn_range_min = models.FloatField(null=True,blank=True)
    dn_range_max = models.FloatField(null=True,blank=True)
    pixels_in_polygon = models.IntegerField(null=True,blank=True)
    pixels_in_range = models.IntegerField(null=True,blank=True)
    pixels_zero = models.IntegerField(null=True,blank=True)
    dn_min = models.FloatField(null=True,blank=True)
    dn_max = models.FloatField(null=True,blank=True)
    avg = models.FloatField(null=True,blank=True)
    
    
    def __unicode__(self):
        return "%s-%s-%s" % (self.country,self.sat,self.year)
        
    def previous(self):
        try:
            previous_records = WorldOriginalSOL.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return WorldOriginalSOL.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = WorldOriginalSOL.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return WorldOriginalSOL.objects.get(id=next_id)
        except:
            return None    
    
    class Meta:
        verbose_name = 'World Original Sum of Lights Records'
        db_table = u'world_original_sol'
        
class WorldCountrySOL(models.Model):
    #    id = models.IntegerField(primary_key=True)
    country = models.ForeignKey('WorldCountry')
    year = models.IntegerField(null=True,blank=True)
    sat = models.CharField(max_length=3)    
    sol = models.IntegerField(null=True,blank=True)
    pixel_count = models.IntegerField(null=True,blank=True)
    dn_mean = models.FloatField(null=True,blank=True)
    dn_stddev = models.FloatField(null=True,blank=True)
    dn_min = models.IntegerField(null=True,blank=True)
    dn_max = models.IntegerField(null=True,blank=True)
    
    def __unicode__(self):
        return "%s-%s-%s" % (self.country,self.sat,self.year)
        
    def previous(self):
        try:
            previous_records = WorldOriginalSOL.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return WorldOriginalSOL.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = WorldOriginalSOL.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return WorldOriginalSOL.objects.get(id=next_id)
        except:
            return None    
    
    class Meta:
        verbose_name = 'World Country Sum of Light'
        db_table = u'world_country_sol'
        
class WorldCountrySOLCali(models.Model):
    #    id = models.IntegerField(primary_key=True)
    country = models.ForeignKey('WorldCountry')
    year = models.IntegerField(null=True,blank=True)
    sat = models.CharField(max_length=3)    
    sol = models.IntegerField(null=True,blank=True)
    pixel_count = models.IntegerField(null=True,blank=True)
    dn_mean = models.FloatField(null=True,blank=True)
    dn_stddev = models.FloatField(null=True,blank=True)
    dn_min = models.IntegerField(null=True,blank=True)
    dn_max = models.IntegerField(null=True,blank=True)
    
    def __unicode__(self):
        return "%s-%s-%s" % (self.country,self.sat,self.year)
        
    def previous(self):
        try:
            previous_records = WorldOriginalSOL.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return WorldOriginalSOL.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = WorldOriginalSOL.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return WorldOriginalSOL.objects.get(id=next_id)
        except:
            return None    
    
    class Meta:
        verbose_name = 'World Country Sum of Light Calibrated'
        db_table = u'world_country_sol_cali'
    