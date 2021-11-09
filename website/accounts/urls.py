from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('user', views.user),
    path('loginPage', views.loginPage),
    path('signup', views.signup),
    path('boxes', views.boxes),
    path('ctf_pi', views.ctf_pi),
    path('ctf_crypto', views.ctf_crypto),
]