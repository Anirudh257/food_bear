from django import forms
from vendor_pages.models import vendor_food_list
from payment.models import order_db

class availability_form(forms.Form):

	# CHOICES = (
	# 		("A", "Available"),
	# 		("NA", "Not-Available"),
	# 	)

	def __init__(self, method, username):

		super(availability_form, self).__init__(method, username)

		food_info = vendor_food_list.objects.filter(vendor_id = username).values_list()

		for item in food_info:
			self.fields[item[2]] = forms.NullBooleanField(required = False, initial = True)
			#forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = self.OPTIONS)
#forms.NullBooleanField(required = False)

class orders_form(forms.Form):

	def __init__(self, method, username):

		super(orders_form, self).__init__(method, username)

		food_order = order_db.objects.filter(status = 'Payment Received', vendor_id = username).values_list()

		for item in food_order:
			self.fields[str(item[0]) + ': ' + item[2]] = forms.NullBooleanField(required = False, initial = True)

			#forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = self.OPTIONS)