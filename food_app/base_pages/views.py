from django.shortcuts import render

# Create your views here.

def home(request):
	context = locals()
	template = 'home.html'
	return render(request, template, context)

def user_home(request, username):
	return render(request, 'user_home.html', {'username' : username})

def vendor_list(request):
	return render(request, 'vendor.html', locals())