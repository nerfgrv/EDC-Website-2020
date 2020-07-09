from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Investor
from .forms import InvestorForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def investors(request):
	context = {
        'investors': Investor.objects.all()
    }
	return render(request,'investors/investorshome.html', context)


def InvestorCreateView(request):
    form = InvestorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('investors')

    context = {
        'form': form
    }
    return render(request, 'investors/create_investor.html', context)


class InvestorDeleteView(DeleteView):
    model = Investor
    success_url = reverse_lazy('investors')
    template_name = 'investors/confirm_delete.html'


class InvestorUpdateView(UpdateView):
    model = Investor
    fields = [
            'company_name',
            'about',
            'contact',
            'email'
        ]
    template_name = 'investors/create_investor.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    
    success_url = reverse_lazy('investors')