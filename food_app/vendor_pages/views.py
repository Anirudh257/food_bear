from django.shortcuts import render, redirect
from vendor_pages.models import vendor_info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .store_item_info import availability_form
from vendor_pages.models import vendor_food_list

# Create your views here.

def list_for_vendors(request, username):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)

	if auth_user is None or user != username + '\n':
		return redirect('/errora')

	ven_inf = vendor_info.objects.get(vendor_id = username)
	form = availability_form(request.POST, username)

	vendor_dict = {'v_id' : ven_inf.vendor_id, 
	'v_name' : ven_inf.vendor_name, 
	'v_i' : ven_inf.img_src,  
	'form' : form}

	if form.is_valid():

		food_info = vendor_food_list.objects.filter(vendor_id = username).values_list()

		for item in food_info:
			temp_tupple = vendor_food_list.objects.get(vendor_id = username, food_item = item[2])
			print(form.cleaned_data[item[2]])
			temp_tupple.available = form.cleaned_data[item[2]]
			temp_tupple.save()

	return render(request, 'vendor_specific.html', vendor_dict)