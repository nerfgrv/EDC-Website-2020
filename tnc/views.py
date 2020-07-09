from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tnc(request):
	return render(request,'tnc/tnchome.html')