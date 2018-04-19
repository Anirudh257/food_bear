from django.db import models

# Create your models here.

class user_details(models.Model):
	username = models.CharField(max_length=30, unique=True)
	email = models.CharField(max_length=30, unique=True)	