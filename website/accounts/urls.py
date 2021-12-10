from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('user_dash', views.user_dash),
    path('loginPage', views.loginPage, name="loginPage"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup', views.signup),
    path('boxes', views.boxes),
    path('ctf_NotSoPi', views.ctf_NotSoPi),
    path('ctf_WhataCapture', views.ctf_WhataCapture),
    path('ctf_LanguageOrSnake', views.ctf_LanguageOrSnake),
    path('vpn_connect', views.vpn_connect),
 
]