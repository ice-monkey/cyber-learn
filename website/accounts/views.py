from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def ctf(request):
    return render(request, 'accounts/ctf.html')

def users(request):
    return render(request, 'accounts/users.html')