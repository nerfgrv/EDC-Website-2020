from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Investor
from .forms import InvestorForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def Investors(request):
	context = {
        'investors': Investor.objects.all()
    }
	return render(request,'investors/investorshome.html', context)


def InvestorCreateView(request):
    if request.user.is_authenticated and request.user.is_team:
        if(request.method == 'POST'):
            form = InvestorForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('investors')
        
        else:
            form = InvestorForm()
        
        context = {
        'form': form
        }
        return render(request, 'investors/create_investor.html', context)

    else:
        return redirect('investors')

@method_decorator(user_passes_test(lambda u: u.is_authenticated and u.is_team), name='dispatch')
class InvestorDeleteView(DeleteView):
    model = Investor
    success_url = reverse_lazy('investors')
    template_name = 'internshipPortal/confirm_delete.html'


def InvestorUpdateView(request, pk):
    if request.user.is_authenticated and request.user.is_team:
        if request.method == 'POST':
            form = InvestorForm(request.POST, request.FILES, instance=Investor.objects.filter(id=pk))
            
            if form.is_valid():
                form.save()
                return redirect('investors')

        form = InvestorForm(instance=Investor.objects.filter(id=pk))
        context = {
            'form': form
        }
        return render(request, 'investors/create_investor.html', context)

    else:
        return redirect('investors')
