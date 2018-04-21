from django.shortcuts import render
from vendor_pages.models import vendor_info

# Create your views here.

def list_for_vendors(request, username):

	ven_inf = vendor_info.objects.get(vendor_id = username)

	food_list = ven_inf.food_items.split(',')

	vendor_dict = {'v_id' : ven_inf.vendor_id, 
	'v_name' : ven_inf.vendor_name, 
	'v_i' : ven_inf.img_src, 
	'f_i' : food_list}

	return render(request, 'vendor_specific.html', vendor_dict)