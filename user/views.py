from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


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
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/signup.html', {'form': form})

def profile(request):
    return render(request, 'user/profile.html')


def logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")
