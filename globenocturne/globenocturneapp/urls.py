from django.conf.urls import patterns, include, url
from djgeojson.views import GeoJSONLayerView
from models import *

urlpatterns = patterns('globenocturneapp.views',
	# Home page URL
	url(r'^home/$','home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=WorldBorder), name='worldborderdata'),
	
	# Query on map click
	url(r'getcountry/$','get_country',name='url_get_country'),	

	# Import Data from CSV
	url(r'dataimport/csv/world_country$','importcsv_world_country'),
	url(r'dataimport/csv/world_population$','importcsv_world_population'),
	url(r'dataimport/csv/world_gdp$','importcsv_world_gdp'),
	url(r'dataimport/csv/world_originsol$','importcsv_world_original_sol'),
	url(r'analysis/world_sol$','analysis_world_sol'),
	url(r'dataimport/csv/world_country_sol$','importcsv_world_country_sol'),
	url(r'dataimport/csv/world_country_sol_cali$','importcsv_world_country_sol_cali'),
)