from typing import NamedTuple
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
	user_name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	#points

class Scoreboard(models.Model):
	pass
	#client

class Flag(models.Model):
	name = models.CharField(max_length=200, null=True, default='')
	description = models.CharField(max_length=200, null=True, default='')
	point = models.IntegerField(default=0, null=True)

class User_points(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	points = models.IntegerField(default=0)

class User_flag(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	flag_object = models.ForeignKey(Flag, null=True, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

