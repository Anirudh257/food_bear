from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from vendor_pages.models import vendor_food_list
from vendor_pages.models import vendor_info
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.

def home(request):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)
	user = user [: len(user) - 1]

	if auth_user is not None:
		return redirect('/account/' + user)

	context = locals()
	template = 'nu_home.html'
	return render(request, template, context)

def user_home(request, username):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)

	if auth_user is None or user != username + '\n':
		return redirect('/errora')

	return render(request, 'u_home.html', {'username' : username})

def vendor_list(request):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)
	user = user [: len(user) - 1]

	if auth_user is not None:
		return redirect('/vendors/' + user)

	vendor_data = vendor_info.objects.filter().values_list()
	render_data = []

	for item in vendor_data:
		v_id = item[1]
		v_user = item[2]
		v_img = item[3]
		render_data.append((v_id, v_user, v_img))

	return render(request, 'nu_list_of_vendors.html', locals())

def user_vendor_list(request, username):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)

	if auth_user is None or user != username + '\n':
		return redirect('/errora')

	vendor_data = vendor_info.objects.filter().values_list()
	render_data = []

	for item in vendor_data:
		v_id = item[1]
		v_user = item[2]
		v_img = item[3]
		render_data.append((v_id, v_user, v_img))

	print(render_data)

	return render(request, 'u_list_of_vendors.html', {'username' : username, 'render_data' : render_data})

def user_order(request, username):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)

	if auth_user is None or user != username + '\n':
		return redirect('/errora')

	return render(request, 'u_MyOrders.html', {'username' : username})

def vendor_dynamic(request, vusername): #change navbar

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)
	user = user [: len(user) - 1]

	if auth_user is not None:
		return redirect('/spec_ven/' + vusername + '/' + user)

	food_list_items = vendor_food_list.objects.filter(vendor_id = vusername).values_list()
	food_dict = {}

	food_dict['vendor_name'] = vendor_info.objects.get(vendor_id = vusername).vendor_name

	food_det = []

	for item in food_list_items:
		if item[3] == 1:
			food_det.append([item[2], item[4]])

	food_dict['food_det'] = food_det

	return render(request, 'nu_dynamic_vendor.html', food_dict)

def user_vendor_dynamic(request, vusername, cusername):

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

			if quant is None or quant == '':
				continue

			if int(quant) == 0:
				continue

			food_ordered.append([item, str(price), int(quant)])

		# proceed to checkout now

		request.session['order'] = food_ordered
		request.session['vendor'] = vusername
		return redirect('/checkout/' + cusername)

	return render(request, 'u_dynamic_vendor.html', food_dict)

def user_profile(request, username):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)

	if auth_user is None or user != cusername + '\n':
		return redirect('/errora')	

	return render(request, 'u_User-Profile.html', locals())

@ensure_csrf_cookie 
def user_checkout(request, username):

	user = request.session['un']
	passw = request.session['pw']

	auth_user = authenticate(username = user, password = passw)

	if auth_user is None or user != username + '\n':
		return redirect('/errora')

	ordered_food = request.session['order']

	if len(ordered_food) == 0:
		return render(request, 'u_Checkout_Page.html', { 'ordered_food' : ordered_food, 'error' : 'Not hungry?'})		

	grand_total = 0

	for item in ordered_food:
		item[1] = float(item[1])
		item.append(item[1] * item[2])
		grand_total += item[3]

	if request.method == 'POST':
		request.session['order_det'] = ordered_food
		request.session['total'] = grand_total
		vendor_id = request.session['vendor']
		return redirect(reverse('payment:process'))

	return render(request, 'u_Checkout_Page.html', { 'ordered_food' : ordered_food, 'grand_total' : grand_total })

def about_us_v(request):
	return render(request, 'about-us.html', {})