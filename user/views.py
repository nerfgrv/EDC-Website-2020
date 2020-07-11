from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import StudentRegisterForm, StartupRegisterForm, StudentUpdateForm, StartupUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, StudentProfile, StartupProfile


def studentregister(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_student     = True
            user.email          = form.cleaned_data.get('email')
            user.save()
            student             = StudentProfile.objects.create(user=user)
            student.city        = form.cleaned_data.get('city')
            student.bio         = form.cleaned_data.get('bio')
            student.college     = form.cleaned_data.get('college')
            student.resume      = form.cleaned_data.get('resume')
            student.contact     = form.cleaned_data.get('contact')
            student.name        = form.cleaned_data.get('name')
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
            user.is_startup         = True
            user.email              = form.cleaned_data.get('email')
            user.save()
            startup                 = StartupProfile.objects.create(user=user)
            startup.startup_name    = form.cleaned_data.get('startup_name')
            startup.city            = form.cleaned_data.get('city')
            startup.founder         = form.cleaned_data.get('founders')
            startup.about           = form.cleaned_data.get('about')
            startup.field_of_work   = form.cleaned_data.get('field_of_work')
            startup.contact         = form.cleaned_data.get('contact')
            startup.website         = form.cleaned_data.get('website')
            startup.image           = form.cleaned_data.get('startup_logo')
            startup.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('startup-login')
    else:
        form = StartupRegisterForm()
    return render(request, 'user/signup-startup.html', {'form': form})


@login_required
def profileupdate(request):
    if request.user.is_student:
        if request.method == 'POST':
            form = StudentUpdateForm(request.POST, request.FILES, instance=request.user.student_profile)

            if form.is_valid():
                form.save()
                messages.success(request, f'Account update successfully!')
                return redirect('home')

        else:
            form = StudentUpdateForm(instance=request.user.student_profile)
        context = {
            'form': form,
        }

    elif request.user.is_startup:
        if request.method == 'POST':
            form = StartupUpdateForm(request.POST, request.FILES, instance=request.user.startup_profile)

            if form.is_valid():
                form.save()
                messages.success(request, f'Account update successfully!')
                return redirect('home')

        else:
            form = StartupUpdateForm(instance=request.user.startup_profile)
        context = {
            'form': form,
        }

    else:
        return redirect('home')

    return render(request, 'user/profile-update.html', context)


@login_required   
def profile(request):
    if request.user.is_student:
        context = {
            'object': request.user.student_profile,
        }

        return render(request, 'user/student_profile.html', context)
    
    elif request.user.is_startup:
        context = {
            'object': request.user.startup_profile,
        }

        return render(request, 'user/startup_profile.html', context)

    else:
        return redirect('home')


@login_required
def logout(request):
	return render(request, 'startupEcosystem/ecosystem-home.html')
