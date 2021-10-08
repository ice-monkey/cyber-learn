from django.db import models

# Create your models here.

class Users(models.Model):
	handle = models.CharField(max_length=200, null=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)	
	date_created = models.DateTimeField(auto_now_add=True, null=True)