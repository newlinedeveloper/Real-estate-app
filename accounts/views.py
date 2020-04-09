from django.shortcuts import render

# Create your views here.

def login(requests):

	if requests.method == 'POST':
		# print('SUBMITTED REG')
		return redirect('login')
	else:
		return render(requests,'accounts/login.html')


def logout(requests):
	return render(requests,'accounts/logout.html')



def register(requests):

	if requests.method == 'POST':
		# print('SUBMITTED REG')
		return redirect('register')
	else:
		return render(requests,'accounts/register.html')

def dashboard(requests):
	return render(requests,'accounts/dashboard.html')
