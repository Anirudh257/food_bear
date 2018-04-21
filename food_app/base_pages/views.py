from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

def home(request):
	context = locals()
	template = 'home.html'
	return render(request, template, context)

def user_home(request, username):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)

	if auth_user is None or user != username + '\n':
		return redirect('/errora')

	return render(request, 'user_home.html', {'username' : username})

def vendor_list(request):
	return render(request, 'vendor.html', locals())