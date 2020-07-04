from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def investors(request):
	return render(request,'investors/investorshome.html')