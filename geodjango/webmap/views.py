from django.shortcuts import render

from django.contrib import admin
from leaflet.admin contrib LeafletGeoAdmin
from .models import MushroomSpot

# Register your models here.

admin.site.register(MushroomSpot, LeafletGeoAdmin) Create your views here.
