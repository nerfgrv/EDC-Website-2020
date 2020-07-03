from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.views.generic import CreateView
from .forms import StudentRegisterForm, StartupRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User


def signup(request):
    return render(request, 'user/templates/signup.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.studentprofile.city = form.cleaned_data.get('city')
            user.studentprofile.bio = form.cleaned_data.get('bio')
            user.studentprofile.college = form.cleaned_data.get('college')
            user.studentprofile.resume = form.cleaned_data.get('resume')
            user.studentprofile.contact = form.cleaned_data.get('contact')
            user.studentprofile.email = form.cleaned_data.get('email')
            user.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login-student')
        else:
            form = UserRegisterForm()
    return render(request, 'user/signup-student.html', {'form': form})

def profile(request):
    return render(request, 'user/profile-student.html')


def registerstup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.startupprofile.name = form.cleaned_data.get('name')
            user.startupprofile.city = form.cleaned_data.get('city')
            user.startupprofile.founder = form.cleaned_data.get('founder')
            user.startupprofile.aboutthestartup = form.cleaned_data.get('about the startup')
            user.startupprofile.fieldofwork = form.cleaned_data.get('field of work')
            user.startupprofile.contact = form.cleaned_data.get('contact')
            user.startupprofile.email = form.cleaned_data.get('email')
            user.startupprofile.website = form.cleaned_data.get('website')
            user.startupprofile.startuplogo = form.cleaned_data.get('startuplogo')
            user.save()
            messages.success(
            request, f'Your account has been created! You are now able to log in')
            return redirect('login-startup')
    else:
        form = UserRegisterForm()
        return render(request, 'user/signup-startup.html', {'form': form})
    
def profilestup(request):
    return render(request, 'user/profile-startup.html')


 
