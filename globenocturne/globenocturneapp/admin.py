from django.contrib.gis import admin
from models import *

class SatYearAdmin(admin.ModelAdmin):
    fields = ['year']
    list_display = ('year',)
admin.site.register(SatYear,SatYearAdmin)

class SatelliteAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id','name')
admin.site.register(Satellite,SatelliteAdmin)

class DMSPProductAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id','name')
admin.site.register(DMSPProduct,DMSPProductAdmin)

class DMSPDatasetAdmin(admin.ModelAdmin):
    fields = ['name','year','satellite','product','wms_layer']
    list_display = ('id','name','year','satellite','product','wms_layer')
admin.site.register(DMSPDataset,DMSPDatasetAdmin)

admin.site.register(WorldBorder,admin.GeoModelAdmin)

class WorldCountryAdmin(admin.ModelAdmin):
    fields = ['fips','iso','iso3digit','name','area_km']
    list_display = ('fips','iso','iso3digit','name','area_km')
admin.site.register(WorldCountry,WorldCountryAdmin)

class WorldPoulationAdmin(admin.ModelAdmin):
    fields = ['country','year','value']
    list_display = ('country','year','value')
admin.site.register(WorldPoulation,WorldPoulationAdmin)

class WorldGDPAdmin(admin.ModelAdmin):
    fields = ['country','year','value']
    list_display = ('country','year','value')
admin.site.register(WorldGDP,WorldPoulationAdmin)

class WorldSOLAdmin(admin.ModelAdmin):
    fields = ['country','year','value']
    list_display = ('country','year','value')
admin.site.register(WorldSOL,WorldSOLAdmin)

class WorldOriginalSOLAdmin(admin.ModelAdmin):    
    fields = ['country','year','sat','sol','dn_range_min','dn_range_max','pixels_in_polygon','pixels_in_range','pixels_zero','dn_min','dn_max','avg']
    list_display = ('country','year','sat','sol','dn_range_min','dn_range_max','pixels_in_polygon','pixels_in_range','pixels_zero','dn_min','dn_max','avg')
admin.site.register(WorldOriginalSOL,WorldOriginalSOLAdmin)
