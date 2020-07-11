from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import InternshipForm, ApplicationForm, VenCapForm
from .models import Internship, InternshipApplication, VentureCapitalist


def Internships(request):
    context = {
        'internships': Internship.objects.all()
    }
    return render(request, 'internshipPortal/Internship.html', context)


def InternshipCreateView(request):
    form = InternshipForm(request.POST or None)
    
    if form.is_valid():
        form.instance.startup = request.user.startup_profile
        form.save()
        return redirect('internships')

    context = {
        'form': form
    }
    return render(request, 'internshipPortal/create_internship.html', context)


def InternshipApplicationView(request, pk):
    internship = Internship.objects.filter(id=pk).first()
    applied_by = InternshipApplication.objects.filter(applied_by=request.user.student_profile)
    for applicant in applied_by:
        if(internship == applicant.internship):
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
    if(request.user.is_student):
        applied_by = InternshipApplication.objects.filter(applied_by=request.user.student_profile)
        for applicant in applied_by:
            if(internship == applicant.internship):
                applied = True
    
    context = {
        'object' : internship,
        'applied' : applied,
    }

    return render(request, 'internshipPortal/internship_detail.html', context)


class InternshipUpdateView(UpdateView):
    model = Internship
    fields = [
            'field_of_internship',
            'duration',
            'about',
            'location',
            'stipend',
            'skills_required',
            'no_of_internships',
            'perks',
            'who_should_apply'
        ]
    template_name = 'internshipPortal/create_internship.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 


class InternshipDeleteView(DeleteView):
    model = Internship
    success_url = reverse_lazy('internships')
    template_name = 'internshipPortal/confirm_delete.html'


#########################################################################


def VenCapitalist(request):
    context = {
        'venture': VentureCapitalist.objects.all()
    }
    return render(request, 'internshipPortal/VentureCapitalist.html', context)


def VenCapCreateView(request):
    form = VenCapForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('venture-capitalist')

    context = {
        'form': form
    }
    return render(request, 'internshipPortal/create_vencap.html', context)

class VenCapUpdateView(UpdateView):
    model = VentureCapitalist
    fields = [
            'company_name',
            'about',
            'contact',
            'email',
        ]
    template_name = 'internshipPortal/create_vencap.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 


class VenCapDeleteView(DeleteView):
    model = VentureCapitalist
    success_url = reverse_lazy('venture-capitalist')
    template_name = 'internshipPortal/confirm_delete.html'


