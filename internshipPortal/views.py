from django.shortcuts import render, redirect
from .forms import InternshipForm, VenCapForm
from .models import Internship
from django.views.generic import DetailView


# Create your views here.
def internships(request):
    context = {
        'internships': Internship.objects.all()
    }
    return render(request, 'internshipPortal/Internship.html', context)

def internship_detail(request):
    return render(request, 'internshipPortal/internship_detail.html', {})


def VentureCapitalist(request):
    return render(request, 'internshipPortal/VentureCapitalist.html', {})


def InternshipCreateView(request):
    form = InternshipForm(request.POST or None)
    if form.is_valid():
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


def VenCapCreateView(request):
    form = VenCapForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('venture-capitalist')

    context = {
        'form': form
    }
    return render(request, 'internshipPortal/create_vencap.html', context)