from django.db import models

# Create your models here.

class Client(models.Model):
	user_name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)