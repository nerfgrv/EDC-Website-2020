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
            student= StudentProfile.objects.create(user=user)
            student.city       = form.cleaned_data.get('city')
            student.bio = form.cleaned_data.get('bio')
            student.college    = form.cleaned_data.get('college')
            student.resume     = form.cleaned_data.get('resume')
            student.contact = form.cleaned_data.get('contact')
            student.email = form.cleaned_data.get('email')
            student.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('student-login')
    else:
        form = StudentRegisterForm()
    return render(request, 'user/signup-student.html', {'form': form})


def startupregister(request):
    if request.method == 'POST' : 
        form = StartupRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.is_startup = True
            startup= StartupProfile.objects.create(user=user)
            startup.startupname = form.cleaned_data.get('name')
            startup.city = form.cleaned_data.get('city')
            startup.founder = form.cleaned_data.get('founder')
            startup.aboutthestartup = form.cleaned_data.get(
                'about the startup')
            startup.fieldofwork     = form.cleaned_data.get('field of work')
            startup.contact         = form.cleaned_data.get('contact')
            startup.email = form.cleaned_data.get('email')
            startup.website = form.cleaned_data.get('website')
            startup.startuplogo = form.cleaned_data.get('startuplogo')
            startup.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('startup-login')
    else:
        form = StartupRegisterForm()
    return render(request, 'user/signup-startup.html', {'form': form})

    
def startupprofile(request):
    return render(request, 'user/profile-startup.html')

def studentprofile(request):
    return render(request, 'user/profile-student.html')
