from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def user(request):
    return render(request, 'accounts/user.html')

def login(request):
    return render(request, 'accounts/login.html')

def boxes(request):
    return render(request, 'accounts/boxes.html')