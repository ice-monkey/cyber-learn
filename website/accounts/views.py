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
from .models import User_flag
from django.db.models.signals import post_save
from django.dispatch import receiver





@login_required

def remove_account(request):
    user = request.user
    user_pk = request.user.pk
    logout(request)
    User.objects.filter(pk=user_pk).delete()
    return redirect('/loginPage')

def dashboard(request):
    scoreboard_objects = User_points.objects.all().order_by('-points')

    usernames = [str(e.user) for e in scoreboard_objects]
    points = [e.points for e in scoreboard_objects]

    user_and_points = zip(usernames, points)

    
    
    if not request.user.is_anonymous:
        current_user = request.user
        get_user = User_points.objects.get(user=current_user)
        user_points = get_user.points
        return render(request, 'accounts/dashboard.html', {'user_and_points':user_and_points, 'user_points':user_points})
    return render(request, 'accounts/dashboard.html')

def user_dash(request):
    scoreboard_objects = User_flag.objects.all().order_by('date_created')

    #username = [str(e.user) for e in scoreboard_objects]
    flag = [e.flag_object for e in scoreboard_objects]
    date_created = [e.date_created for e in scoreboard_objects]

    user_and_flag = zip(flag, date_created)
    current_user = request.user
    get_user = User_points.objects.get(user=current_user)
    user_points = get_user.points
    
        
    return render(request, 'accounts/user_dash.html', {'user_points':user_points, 'user_and_flag':user_and_flag})

def loginPage(request):
    if 'next' in request.GET:
        messages.add_message(request, messages.INFO, 'You must be signed in to view this page')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
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
    current_user = request.user
    get_user = User_points.objects.get(user=current_user)
    user_points = get_user.points
    return render(request, 'accounts/boxes.html', {'user_points':user_points})

@login_required(login_url='loginPage')
def ctf_NotSoPi(request):
    current_user = request.user
    get_user = User_points.objects.get(user=current_user)
    user_points = get_user.points
    if request.method == "POST":
        flag = request.POST.get('flag')
        flag_db = Flag.objects.get(description=flag)
        get_user = request.user
        
        if User_flag.objects.filter(flag_object=flag_db, user=get_user).exists():
            print("flag nope")
        else:
            print("flag juhuu")
        
            points = flag_db.point
            if flag == flag_db.description:
                user = User_points.objects.get(user=get_user)
                User_flag.objects.create(user=get_user, flag_object=flag_db)
                user.points += points
                user.save()
            return redirect('/ctf_NotSoPi')

    return render(request, 'accounts/challenges/ctf_NotSoPi.html', {'user_points':user_points})


@login_required(login_url='loginPage')
def ctf_WhataCapture(request):
    return render(request, 'accounts/challenges/ctf_WhataCapture.html')

@login_required(login_url='loginPage')
def ctf_LanguageOrSnake(request):
    return render(request, 'accounts/challenges/ctf_LanguageOrSnake.html')

@login_required(login_url='loginPage')
def vpn_connect(request):
    return render(request, 'accounts/vpn_connect.html')