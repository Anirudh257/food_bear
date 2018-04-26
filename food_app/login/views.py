from django.shortcuts import render, redirect
from .login_details import user_login_details
from .signup_details import user_signup_details
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from base_pages import templates as home_temp
from login.models import user_details

# Create your views here.

def login(request):
	
	request.session['un'] = 'sajncjasnckljasnl'
	request.session['pw'] = 'acubkajcsbkcs'

	form = user_login_details(request.POST or None)

	if form.is_valid():

		fusername = form.cleaned_data['username'] + '\n'
		fpassword = form.cleaned_data['password'] + '\n'

		request.session['un'] = fusername
		request.session['pw'] = fpassword

		a_user = fusername [:len(fusername) - 1]

		if fusername in ['chai' + '\n', 'ge' + '\n', 'surya' + '\n', 'roll' + '\n', 'rama' + '\n']:
			return redirect("/ven/" + a_user + "/")

		return redirect("/account/" + a_user + "/")

	context = locals()
	template = 'LoginPage.html'
	return render(request, template, context)

def signup(request):

	form = user_signup_details(request.POST or None)

	if form.is_valid():

		susername = form.cleaned_data['username'] + '\n'
		spassword = form.cleaned_data['password'] + '\n'
		semail = form.cleaned_data['email'] + '\n'

		user = User.objects.create_user(susername, semail, spassword)
		user.save()

		# user_det = user_details(username = susername, email = semail)
		# user_det.save()

		return redirect("/login")

	context = locals()
	template = 'SignUpPage.html'
	return render(request, template, context)

def access_error(request):
	return render(request, 'error_access.html', locals())