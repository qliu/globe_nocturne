from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.gis.db import models

# Import from general utilities
from util import *

# Aggregation Functions
from django.db.models import Count, Avg

# GeoDjango Imports
from django.contrib.gis.geos import Point

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
    
'''-------------
Spatial Query
-------------'''
def get_country(request):
    if request.method == 'POST':
        if request.POST["latlng"] and request.POST["latlng"] != "":
            latlng = request.POST["latlng"][7:-1].split(", ")
            lat = float(latlng[0])
            lng = float(latlng[1])
            pnt = Point(lng,lat,srid=4326)
            try:
                cntry = WorldBorder.objects.filter(geom__contains=pnt)[0]
                country_name = cntry.country
                country_iso = cntry.iso
                
                country = WorldCountry.objects.get(iso=country_iso)
                country_pop_all = WorldPoulation.objects.filter(country=country.id)
                country_data_list = []
                country_year_list = []
                country_total_sol_list = {}
                country_num_sol_list = {}
                for cpop in country_pop_all:
                    if cpop.year >= 1992 and cpop.year <= 2010:
                        country_data_list.append({"country":cpop.country.name,"year":cpop.year,"pop":cpop.value})
                        country_year_list.append(cpop.year)
                        country_total_sol_list[cpop.year] = 0
                        country_num_sol_list[cpop.year] = 0
#                final_data_list = sorted(country_data_list,key=lambda x:x[1]["year"])
##                print country_data_list
#                print final_data_list
                country_sol_all = WorldCountrySOL.objects.filter(country=country.id)
#                print country_sol_all
                for index,csol in enumerate(country_sol_all):
#                    print csol.year
                    if csol.year >= 1992 and csol.year <= 2010:
                        country_total_sol_list[csol.year] += csol.sol
#                        print country_total_sol_list[csol.year]
                        country_num_sol_list[csol.year] += 1
#                print country_total_sol_list
#                print country_num_sol_list
                for index,y in enumerate(country_year_list):
                    country_data_list[index]["sol"] = float(country_total_sol_list[y])/float(country_num_sol_list[y])
                print "country_data_list: ",country_data_list
            except Exception as e:
                print e
                country_name = "Country not found"

            response_data = {"country":country_name,"data":json.dumps(country_data_list)}
    return HttpResponse(json.dumps(response_data),content_type="application/json")

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
GLOBAL_NOCTURNE_DATA_PATH = "C:/QLiu/Devl/globe_nocturne/globenocturne/globenocturneapp/static/data/csv/" # use this for localhost
#GLOBAL_NOCTURNE_DATA_PATH = '/opt/bitnami/apps/django/django_project/globe_nocturne/globenocturne/globenocturneapp/static/data/csv/' # use this for server
# Import World Countries
def importcsv_world_country(request):
    try:
        with open(GLOBAL_NOCTURNE_DATA_PATH+"world_country_list.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    world_country = WorldCountry(
                        id=int(row[0].strip()),
                        fips=row[1].strip(),
                        iso=row[2].strip() if row[2] != "" else None,
                        iso3digit=row[3].strip() if row[3] != "" else None,
                        name=row[4].strip() if row[4] != "" else None,
                        capital=row[5].strip() if row[5] != "" else None,
                        continent=row[6].strip() if row[6] != "" else None
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
                            pop = float(value)
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
                            pop = float(value)
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
    
# Import World Country SOL (before intercalibration)
def importcsv_world_country_sol(request):
    try:
        with open(GLOBAL_NOCTURNE_DATA_PATH+"sol_country.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    cntry = WorldCountry.objects.get(fips=row[0])
                    wcs = WorldCountrySOL(
                        country=cntry,
                        sat=row[1].strip() if row[1] != "" else None,
                        year=row[2].strip() if row[2] != "" else None,
                        sol=int(row[4].strip()) if row[4] != "" else None,
                        pixel_count=int(row[3].strip()) if row[3] != "" else None,
                        dn_mean=float(row[5].strip()) if row[5] != "" else None,
                        dn_stddev=float(row[6].strip()) if row[6] != "" else None,
                        dn_min=float(row[7].strip()) if row[7] != "" else None,
                        dn_max=float(row[8].strip()) if row[8] != "" else None
                    )
                    wcs.save()
        return HttpResponse("World Country SOL - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("World Country SOL - Import Failed! Error: %s" % e)
    
# Import World Country SOL (before intercalibration)
def importcsv_world_country_sol_cali(request):
    try:
        with open(GLOBAL_NOCTURNE_DATA_PATH+"sol_country_cali.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    cntry = WorldCountry.objects.get(fips=row[0])
                    wcs = WorldCountrySOLCali(
                        country=cntry,
                        sat=row[1].strip() if row[1] != "" else None,
                        year=row[2].strip() if row[2] != "" else None,
                        sol=int(row[4].strip()) if row[4] != "" else None,
                        pixel_count=int(row[3].strip()) if row[3] != "" else None,
                        dn_mean=float(row[5].strip()) if row[5] != "" else None,
                        dn_stddev=float(row[6].strip()) if row[6] != "" else None,
                        dn_min=float(row[7].strip()) if row[7] != "" else None,
                        dn_max=float(row[8].strip()) if row[8] != "" else None
                    )
                    wcs.save()
        return HttpResponse("World Country SOL Cali - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("World Country SOL Cali - Import Failed! Error: %s" % e)