from django.urls import path
from cybersite import views

urlpatterns = [
    path('', views.cybersite, name='index'),
]
