from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


from listings.models import Listing
from realtors.models import Realtor 


def index(requests):
	listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]

	context = {

	'listings' : listings

	}
	return render(requests,"pages/index.html",context)

def about(requests):
	#Get all realtors
	realtors = Realtor.objects.order_by('-hire_date')

	#Get MVP
	mvp_realtors = Realtor.objects.all().filter(is_mvp = True)

	context = {

	'realtors' :realtors,
	'mvp_realtors': mvp_realtors
	}

	return render(requests,"pages/about.html",context)
