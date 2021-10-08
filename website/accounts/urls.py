from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('ctf/', views.ctf),
    path('users', views.users),
]