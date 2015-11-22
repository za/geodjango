from django.db import models
from djgeojson.fields import PointField

# Create your models here.

class MushroomSpot(models.Model):
	geom = PointField()

	def __str__(self):
		return("%s" % self.geom)
