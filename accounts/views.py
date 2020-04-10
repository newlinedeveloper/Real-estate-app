from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def login(requests):

	if requests.method == 'POST':
		# print('SUBMITTED REG')
		messages.error(requests,'Testing error message')
		return redirect('login')
	else:
		return render(requests,'accounts/login.html')


def logout(requests):
	return render(requests,'accounts/logout.html')



def register(requests):

	if requests.method == 'POST':
		# print('SUBMITTED REG')
		messages.error(requests,'Testing error message')
		return redirect('register')
	else:
		return render(requests,'accounts/register.html')

def dashboard(requests):
	return render(requests,'accounts/dashboard.html')
