from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

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

		first_name = requests.POST['first_name']
		last_name = requests.POST['last_name']
		username = requests.POST['username']
		email = requests.POST['email']
		password = requests.POST['password']
		password2 = requests.POST['password2']
		
		# check passwords
		if password == password2:
			# check username
			if User.objects.filter(username=username).exists():
				messages.error(requests,'That username is taked')
				return redirect('register')
			else:
				if User.objects.filter(email = email).exists():
					messages.error(requests,'That email is being used')
					return redirect('register')
				else:
					 user = User.objects.create_user(username = username,password = password,email=email,first_name=first_name,last_name =last_name)
					 auth.login(requests,user)
					 messages.success(requests,'You are now logged in')
					 return redirect('login')
		else:
			messages.error(requests,"Passwords are not match")

		# print('SUBMITTED REG')
		messages.error(requests,'Testing error message')
		return redirect('register')
	else:
		return render(requests,'accounts/register.html')

def dashboard(requests):
	return render(requests,'accounts/dashboard.html')
