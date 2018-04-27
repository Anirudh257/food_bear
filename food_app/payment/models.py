from django.db import models

# Create your models here.

class order_db(models.Model):
	order_id = models.IntegerField(primary_key = True)
	user = models.CharField(max_length=30)
	item_list = models.CharField(max_length=255)
	grand_total = models.CharField(max_length=30)
	status = models.CharField(max_length=30, default = 'N/A')
	vendor_id = models.CharField(max_length=30, default = 'N/A')
