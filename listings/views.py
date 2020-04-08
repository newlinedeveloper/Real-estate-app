from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
from .models import Listing


def  index(requests):

	listings = Listing.objects.order_by('-list_date').filter(is_published=True)

	paginator = Paginator(listings,6)
	page = requests.GET.get('page')
	paged_listings = paginator.get_page(page)


	context = {
	'listings' : paged_listings
	} 

	return render(requests,'listings/listings.html',context)


def  listing(requests,listing_id):
	return render(requests,'listings/listing.html')


def  search(requests):
	return render(requests,'listings/listing.html')