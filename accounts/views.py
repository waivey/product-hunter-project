from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error':'Username already taken.'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				auth.login(request,user)
				return redirect('home')
		else:
			return render(request, 'accounts/signup.html', {'error2':'Passwords must match.'})
	else:
		return render(request, 'accounts/signup.html')

def login(request):
	return render(request, 'accounts/login.html')

def logout(request):
	# Need to route to homepage after logging out
	return render(request, 'accounts/logout.html')

