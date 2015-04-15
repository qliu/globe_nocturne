from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.gis.db import models

# Import from general utilities
from util import *

from globenocturneapp.models import *

'''-----------------------
Home Page
-----------------------'''
# Home page
@render_to("globenocturneapp/home.html")
def home(request):
    return {}