from django.shortcuts import render

# Create your views here.
def NavBar(request):
	return render(request, 'home/base.html', )