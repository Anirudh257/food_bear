from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from vendor_pages.models import vendor_food_list
from vendor_pages.models import vendor_info
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
	return render(request, 'sort-by-vendor.html', locals())

def user_order(request, username):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)

	if auth_user is None or user != username + '\n':
		return redirect('/errora')

	return render(request, 'MyOrders.html', {'username' : username})

def vendor_dynamic(request, vusername, cusername):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)

	if auth_user is None or user != cusername + '\n':
		return redirect('/errora')	

	food_list_items = vendor_food_list.objects.filter(vendor_id = vusername).values_list()
	food_dict = {}

	food_dict['vendor_name'] = vendor_info.objects.get(vendor_id = vusername).vendor_name

	food_det = []

	for item in food_list_items:
		if item[3] == 1:
			food_det.append([item[2], item[4]])

	food_dict['food_det'] = food_det
	food_dict['username'] = cusername


	if request.method == 'POST':

		food_ordered = []

		for item, price in food_det:
			
			quant = request.POST.get(item, None)

			if quant == '':
				continue

			food_ordered.append([item, price, int(quant)])

		# proceed to checkout now

	return render(request, 'dynamic_vendor.html', food_dict)

def item_list(request):
	return render(request, 'list-item.html', locals())