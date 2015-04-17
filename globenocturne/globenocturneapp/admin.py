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