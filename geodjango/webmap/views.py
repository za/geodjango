from django.shortcuts import render

# Register your models here.
from .models import MushroomSpot

def home(request):
	alist = []

	mushroomspots = MushroomSpot.objects.all()
	for mushroomspot in mushroomspots:
		alist.append(mushroomspot)

	context_dict = {'qs_results': alist}

	return render(request, 'map.html', context_dict)
