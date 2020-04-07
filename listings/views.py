from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def  index(requests):
	return render(requests,'listings/listings.html')


def  listing(requests):
	return render(requests,'listings/listing.html')


def  search(requests):
	return render(requests,'listings/listing.html')