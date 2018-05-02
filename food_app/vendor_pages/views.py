from django.shortcuts import render, redirect
from vendor_pages.models import vendor_info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .store_item_info import availability_form
from .store_item_info import orders_form
from vendor_pages.models import vendor_food_list
from payment.models import order_db

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

def order_status(request, username):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)

	if auth_user is None or user != username + '\n':
		return redirect('/errora')

	ven_inf = vendor_info.objects.get(vendor_id = username)

	orders_in_trans_db = order_db.objects.filter(status = 'Payment Received', vendor_id = username).values_list()
	orders_done_db = order_db.objects.filter(status = 'Done', vendor_id = username).values_list()

	form = orders_form(request.POST, username)

	vendor_dict = {'v_id' : ven_inf.vendor_id, 
	'v_name' : ven_inf.vendor_name, 
	'v_i' : ven_inf.img_src,  
	'orders_in_trans_db' : orders_in_trans_db, 
	'orders_done_db' : orders_done_db,
	'form' : form }

	if form.is_valid():
		
		food_orders = order_db.objects.filter(status = 'Payment Received', vendor_id = username).values_list()

		for item in food_orders:
			val = form.cleaned_data[str(item[0]) + ': ' + item[2]]

			if val == 1:
				tupple = order_db.objects.get(order_id = item[0])
				tupple.status = 'Done'
				tupple.save()

	return render(request, 'OrderReady.html', vendor_dict)