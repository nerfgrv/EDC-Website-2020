from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from .forms import StudentRegisterForm, StartupRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, StudentProfile, StartupProfile

def studentregister(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.is_student = True
            StudentProfile.objects.create(user=user)
            user.student_profile.city       = form.cleaned_data.get('city')
            user.student_profile.bio        = form.cleaned_data.get('bio')
            user.student_profile.college    = form.cleaned_data.get('college')
            user.student_profile.resume     = form.cleaned_data.get('resume')
            user.student_profile.contact    = form.cleaned_data.get('contact')
            user.student_profile.email      = form.cleaned_data.get('email')
            user.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('student-login')
    else:
        form = StudentRegisterForm()
    return render(request, 'user/signup-student.html', {'form': form})


def startupregister(request):
    if request.method == 'POST':
        form = StartupRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.is_startup = True
            StartupProfile.objects.create(user=user)
            user.startup_profile.name            = form.cleaned_data.get('name')
            user.startup_profile.city            = form.cleaned_data.get('city')
            user.startup_profile.founder         = form.cleaned_data.get('founder')
            user.startup_profile.aboutthestartup = form.cleaned_data.get('about the startup')
            user.startup_profile.fieldofwork     = form.cleaned_data.get('field of work')
            user.startup_profile.contact         = form.cleaned_data.get('contact')
            user.startup_profile.email           = form.cleaned_data.get('email')
            user.startup_profile.website         = form.cleaned_data.get('website')
            user.startup_profile.startuplogo     = form.cleaned_data.get('startuplogo')
            user.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('startup-login')
    else:
        form = StartupRegisterForm()
    return render(request, 'user/signup-startup.html', {'form': form})

    
def startupprofile(request):
    return render(request, 'user/profile-startup.html')

def studentprofile(request):
    return render(request, 'user/profile-student.html')
