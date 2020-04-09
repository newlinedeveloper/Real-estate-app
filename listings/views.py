from django.shortcuts import render,get_object_or_404
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

	listing = get_object_or_404(Listing,pk=listing_id)

	context = {

		'listing' : listing
	}
	return render(requests,'listings/listing.html',context)


def  search(requests):

	queryset_list = Listing.objects.order_by('-list_date')


	if 'keywords' in requests.GET:
		keywords = request.GET('keywords')

	if keywords:
		queryset_list = queryset_list.filter(description_icontains=keywords)

	context ={
		'listings' : queryset_list
	}

	return render(requests,'listings/listing.html',context)	
