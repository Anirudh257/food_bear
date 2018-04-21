from django.db import models

# Create your models here.

class vendor_info(models.Model):
	vendor_id = models.CharField(max_length=30, unique=True)
	vendor_name = models.CharField(max_length=30, unique=True)
	img_src = models.CharField(max_length = 255)
	food_items = models.CharField(max_length = 255)
