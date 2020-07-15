from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import InternshipForm, ApplicationForm, VenCapForm
from .models import Internship, InternshipApplication, VentureCapitalist
import datetime


def Internships(request):
    context = {
        'internships': Internship.objects.all()
    }
    return render(request, 'internshipPortal/Internship.html', context)

def MyInternships(request):
    if(request.user.is_authenticated and request.user.is_startup):
        internships = Internship.objects.filter(startup=request.user.startup_profile)
        context = {
            'internships': internships,
        }
        return render(request, 'internshipPortal/Internship.html', context)
    elif(request.user.is_authenticated and request.user.is_student):
        internships = InternshipApplication.objects.filter(applied_by=request.user.student_profile)
        for internship in internships:
            print(internship)
        context = {
            'internships': internships,
        }
        return render(request, 'internshipPortal/MyInternship.html', context)
    else:
        redirect(internships)
    
    

def InternshipCreateView(request):
    form = InternshipForm(request.POST or None)
    if request.user.is_authenticated and request.user.is_startup:
        if form.is_valid():
            form.instance.startup = request.user.startup_profile
            form.save()
            return redirect('internships')
    else:
        messages.success(request, f'You are not authorised to access this page.')
        return redirect('internships')

    context = {
        'form': form
    }
    return render(request, 'internshipPortal/create_internship.html', context)


def InternshipApplicationView(request, pk):
    internship = Internship.objects.filter(id=pk).first()
    applied_by = InternshipApplication.objects.filter(applied_by=request.user.student_profile)
    date = datetime.date.today()
    for applicant in applied_by:
        if(internship == applicant.internship):
            messages.success(request, f'You have already applied for that internship.')
            return redirect('internship-detail', pk)
    
    if(date > internship.apply_by):
        messages.success(request, f'You have can not apply for this internship.')
        return redirect('internship-detail', pk)

    form = ApplicationForm(request.POST or None)
    
    if form.is_valid():
        form.instance.internship = Internship.objects.filter(id = pk).first()
        form.instance.applied_by = request.user.student_profile
        form.save()
        return redirect('internship-detail', pk)

    context = {
        'form': form
    }
    return render(request, 'internshipPortal/create_internship.html', context)



def InternshipDetailView(request, pk):
    applied = False

    internship = Internship.objects.filter(id=pk).first()
    if(request.user.is_authenticated and request.user.is_student):
        applied_by = InternshipApplication.objects.filter(applied_by=request.user.student_profile)
        for applicant in applied_by:
            if(internship == applicant.internship):
                applied = True
    
    context = {
        'object' : internship,
        'applied' : applied,
    }

    return render(request, 'internshipPortal/internship_detail.html', context)


def InternshipUpdateView(request, pk):
    if request.user.is_authenticated and request.user.is_startup and (request.user.startup_profile == Internship.objects.filter(id=pk).first().startup):
        if request.method == 'POST':
            form = InternshipForm(request.POST, instance=Internship.objects.filter(id=pk).first())
            
            if form.is_valid():
                form.save()
                return redirect('internships')

        form = InternshipForm(instance=Internship.objects.filter(id=pk).first())
        context = {
            'form': form
        }
        return render(request, 'internshipPortal/create_internship.html', context)

    else:
        messages.success(request, f'You are not authorised to access this page.')
        return redirect('internships')


def InternshipDeleteView(request, pk): 
    obj = get_object_or_404(Internship, id=pk)
    internship = Internship.objects.filter(id=pk).first()
    if request.user.is_authenticated and request.user.is_startup and (request.user.startup_profile == obj.startup):
        if request.method =="POST":  
            obj.delete()  
            return redirect("internship-detail") 
    else:
        messages.success(request, f'You are not authorised to access this page')
        return redirect('internship-detail', pk)
    
    context ={
        'object' : internship
    }
  
    return render(request, "delete_view.html", context) 



#########################################################################


def VenCapitalist(request):
    context = {
        'venture': VentureCapitalist.objects.all()
    }
    return render(request, 'internshipPortal/VentureCapitalist.html', context)


def VenCapCreateView(request):
    if request.user.is_authenticated and request.user.is_team:
        if(request.method == 'POST'):
            form = VenCapForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('venture-capitalist')
        
        else:
            form = VenCapForm()
        
        context = {
        'form': form
        }
        return render(request, 'internshipPortal/create_vencap.html', context)

    else:
        return redirect('venture-capitalist')

def VenCapUpdateView(request, pk):
    if request.user.is_authenticated and request.user.is_team:
        if request.method == 'POST':
            form = VenCapForm(request.POST, request.FILES, instance=VentureCapitalist.objects.filter(id=pk))
            
            if form.is_valid():
                form.save()
                return redirect('venture-capitalist')

        form = VenCapForm(instance=VentureCapitalist.objects.filter(id=pk))
        context = {
            'form': form
        }
        return render(request, 'internshipPortal/create_vencap.html', context)

    else:
        return redirect('venture-capitalist')

@method_decorator(user_passes_test(lambda u: u.is_authenticated and u.is_team), name='dispatch')
class VenCapDeleteView(DeleteView):
    model = VentureCapitalist
    success_url = reverse_lazy('venture-capitalist')
    template_name = 'internshipPortal/confirm_delete.html'


