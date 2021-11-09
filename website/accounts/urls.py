from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('user', views.user),
    path('login', views.login),
    path('registrer', views.registrer),
    path('boxes', views.boxes),
    path('ctf_pi', views.ctf_pi),
    path('ctf_crypto', views.ctf_crypto),
]