from django.db import models
from djgeojson.fields import PointField

# Create your models here.

class MushroomSpot(models.Model):
	geom = PointField()

