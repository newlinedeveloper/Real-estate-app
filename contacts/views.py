from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contacts

# Create your views here.


def contact(requests):

	if requests.method == 'POST':
		listing_id = requests.POST['listing_id']
		listing = requests.POST['listing']
		name = requests.POST['name']
		email = requests.POST['email']
		phone = requests.POST['phone']
		message = requests.POST['message']
		user_id = requests.POST['user_id']
		realtor_email = requests.POST['realtor_email']

		contact = Contacts(listing = listing, listing_id=listing_id, name=name, email=email,phone=phone,message=message,user_id=user_id)
		

		contact.save()


		messages.success(requests,"your request has been submitted, a realtor will get bact to you soon") 

		return redirect('listings/'+listing_id)