from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.gis.db import models

# Import from general utilities
from util import *

# Aggregation Functions
from django.db.models import Count, Avg

from globenocturneapp.models import *

'''-----------------------
Home Page
-----------------------'''
# Home page
@render_to("globenocturneapp/home.html")
def home(request):
    satyears = SatYear.objects.all()
    satellites = Satellite.objects.all()
    dmsp_products = DMSPProduct.objects.all()
    dmsp_datasets = DMSPDataset.objects.all()
    return {
        "satyears":satyears,
        "satellites":satellites,
        "dmsp_products":dmsp_products,
        "dmsp_datasets":dmsp_datasets,
    }

'''------------------
Data Analysis
------------------'''
def analysis_world_sol(request):
    try:
        original_sol = WorldOriginalSOL.objects.all()
        sol1 = WorldOriginalSOL.objects.values('country','year').annotate(sumoflight=Avg('sol'))
        for s in sol1:
            world_sol = WorldSOL(
                country=WorldCountry.objects.get(id=s['country']),
                year=s['year'],
                value=s['sumoflight'],
            )
            world_sol.save()         
        return HttpResponse("World Country - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("World Country - Import Failed! Error: %s" % e)    


'''------------------
Import data from CSV
------------------'''
GLOBAL_NOCTURNE_DATA_PATH = "C:/QLiu/Devl/globe_nocturne/globenocturne/globenocturneapp/data/csv/" # use this for localhost
#GLOBAL_NOCTURNE_DATA_PATH = '/opt/bitnami/apps/django/django_project/globe_nocturne/globenocturne/globenocturneapp/data/csv/' # use this for server
# Import World Countries
def importcsv_world_country(request):
    try:
        with open(GLOBAL_NOCTURNE_DATA_PATH+"world_countries.csv",'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                world_country = WorldCountry(
                    fips=row[0].strip(),
                    iso=row[1].strip(),
                    name=row[2].strip(),
                    area_km=row[3].strip()
                )
                world_country.save()
        return HttpResponse("World Country - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("World Country - Import Failed! Error: %s" % e)
    
# Import World Countries
def importcsv_world_population(request):
    try:
        with open(GLOBAL_NOCTURNE_DATA_PATH+"world_population.csv",'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                country_iso = row[0]
                try:
                    country=WorldCountry.objects.get(iso3digit=country_iso)
                except:
                    country=None
                for index,value in enumerate(row):
                    if index > 0 and country:
                        if value:
                            pop = float()
                        else:
                            pop = None
                        world_population = WorldPoulation(
                            country=country,
                            year=1960+index-1,
                            value=pop
                        )
                        world_population.save()
        return HttpResponse("World Population - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("World Population - Import Failed! Error: %s" % e)

# Import World Countries
def importcsv_world_gdp(request):
    try:
        with open(GLOBAL_NOCTURNE_DATA_PATH+"world_gdp.csv",'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                country_iso = row[0]
                try:
                    country=WorldCountry.objects.get(iso3digit=country_iso)
                except:
                    country=None
                for index,value in enumerate(row):
                    if index > 0 and country:
                        if value:
                            pop = float()
                        else:
                            pop = None
                        world_gdp = WorldGDP(
                            country=country,
                            year=1960+index-1,
                            value=pop
                        )
                        world_gdp.save()
        return HttpResponse("World GDP - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("World GDP - Import Failed! Error: %s" % e)
    
# Import World Countries Original SOL
def importcsv_world_original_sol(request):
    try:
        with open(GLOBAL_NOCTURNE_DATA_PATH+"world_countries_original_som.csv",'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                for index,value in enumerate(row):
                    try:
                        country = WorldCountry.objects.get(fips=row[0])
                    except:
                        country = None
                    world_sol = WorldOriginalSOL(
                        country = country,
                        year = int(row[1]),
                        sat = row[2],
                        sol = float(row[3]),
                        dn_range_min = float(row[4].split(" ")[0]),
                        dn_range_max = float(row[4].split(" ")[1]),
                        pixels_in_polygon = float(row[5]),
                        pixels_in_range = float(row[6]),
                        pixels_zero = float(row[7]),
                        dn_min = float(row[8]),
                        dn_max = float(row[9]),
                        avg = float(row[10])
                    )
                    world_sol.save()
        return HttpResponse("World Original SOL - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("World Original SOL - Import Failed! Error: %s" % e)