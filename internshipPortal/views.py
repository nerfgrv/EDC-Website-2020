from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InternshipForm, VenCapForm
from .models import Internship, VentureCapitalist
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def internships(request):
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

class InternshipDetailView(DetailView):
    model = Internship
    template_name = 'internshipPortal/internship_detail.html'
    queryset = Internship.objects.all()

class InternshipUpdateView(UpdateView):
    model = Internship
    fields = [
            'company_name',
            'fields_of_work',
            'duration',
            'about',
            'location',
            'stipend',
            'skills_required',
            'no_of_internships',
            'perks',
            'who_can_apply'
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


