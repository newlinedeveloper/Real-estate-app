from django.shortcuts import render

# Create your views here.

def login(requests):
	return render(requests,'accounts/login.html')

def logout(requests):
	return render(requests,'accounts/logout.html')



def register(requests):
	return render(requests,'accounts/register.html')

def dashboard(requests):
	return render(requests,'accounts/dashboard.html')
