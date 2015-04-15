from django.conf.urls import patterns, include, url
from djgeojson.views import GeoJSONLayerView
from models import *

urlpatterns = patterns('globenocturneapp.views',
	# Home page URL
	url(r'^home/$','home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=WorldBorder), name='worldborderdata'),
)