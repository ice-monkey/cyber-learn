from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Client)
admin.site.register(Scoreboard)
admin.site.register(Flag)
admin.site.register(User_points)