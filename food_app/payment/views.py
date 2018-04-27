from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from payment.models import order_db
from django.views.decorators.csrf import csrf_exempt
from payment.models import order_db

# Create your views here.

@csrf_exempt
def payment_done(request):

	success_entry = order_db.objects.get(order_id = request.session['o_id'])
	success_entry.status = 'Payment Received'
	success_entry.save()

	return render(request, 'done.html', {})


@csrf_exempt
def payment_canceled(request):

	return render(request, 'canceled.html', {})

def payment_process(request):

	order_det = request.session['order_det']
	order_total = request.session['total']
	user = request.session['un']
	user = user [: len(user) - 1]

	items = ''

	for item in order_det:
		items = items + item[0] + ', '

	items = items [: len(items) - 2]

	prev_data = order_db.objects.filter().values_list()
	o_id = prev_data[len(prev_data) - 1][0] + 1
	request.session['o_id'] = o_id

	db_data = order_db(order_id = o_id, user = user, item_list = items, grand_total = order_total, status = 'In Transaction', vendor_id = request.session['vendor'])
	db_data.save()

	if db_data == 0:
		pass

	order = get_object_or_404(order_db, order_id = o_id)	
	host = request.get_host()

	paypal_dict = {

		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'amount': order_total,
		'item_name': 'Order ' + str(o_id),
		'invoice': 'Order {}'.format(order.order_id),
		'currency_code': 'USD',
		'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
		'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
		'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
	}

	form = PayPalPaymentsForm(initial = paypal_dict)
	return render(request, 'process.html', {'order' : order, 'form': form })

	# order = get_object_or_404(order_db, )
	#return render(request, 'temp.html', {})
