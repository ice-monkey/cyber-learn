from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def user(request):
    return render(request, 'accounts/user.html')

def login(request):
    return render(request, 'accounts/login.html')

def signup(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html')

def boxes(request):
    return render(request, 'accounts/boxes.html')

def ctf_pi(request):
    return render(request, 'accounts/challenges/ctf_pi.html')

def ctf_crypto(request):
    return render(request, 'accounts/challenges/ctf_crypto.html')