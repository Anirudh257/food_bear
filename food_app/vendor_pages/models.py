from django.db import models

# Create your models here.

class vendor_info(models.Model):
	vendor_id = models.CharField(max_length=30, unique=True)
	vendor_name = models.CharField(max_length=30, unique=True)
	img_src = models.CharField(max_length = 255)

class vendor_food_list(models.Model):
	vendor_id = models.CharField(max_length=30)
	food_item = models.CharField(max_length = 255)
	available = models.NullBooleanField(default = False)
	price = models.DecimalField(max_digits=6, decimal_places=2, default = 0.00)
