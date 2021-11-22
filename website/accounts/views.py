from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .models import Flag
from .models import User_points
from django.db.models.signals import post_save
from django.dispatch import receiver


def home(request):
    return render(request, 'accounts/dashboard.html')

def user_dash(request):
    current_user = request.user
    get_user = User_points.objects.get(user=current_user)
    user_points = get_user.points
    print(user_points)
        

    return render(request, 'accounts/user_dash.html', {'user_points':user_points})

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/boxes')
        else:
            messages.info(request, "Username or password is incorrect")
            
    context = {}
    return render(request, 'accounts/loginPage.html')

def signup(request):
    form = CreateUserForm()
    

    if request.method == "POST":
        form = CreateUserForm(request.POST)
    
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}' )
            return redirect('/loginPage')
            
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)

@receiver(post_save, sender=User)
def create_user_picks(sender, instance, created, **kwargs):
    if created:
        User_points.objects.create(user=instance)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def boxes(request):
    return render(request, 'accounts/boxes.html')

@login_required(login_url='loginPage')
def ctf_pi(request):
    if request.method == "POST":
        flag = request.POST.get('flag')
        flag_db = Flag.objects.get(name='flag1')
        if flag == flag_db.description:
            return redirect('/loginPage')

    return render(request, 'accounts/challenges/ctf_pi.html')

@login_required(login_url='loginPage')
def ctf_crypto(request):
    return render(request, 'accounts/challenges/ctf_crypto.html')


