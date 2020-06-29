from django.shortcuts import render

# Create your views here.
def events(request):
    return render(request,'event/events.html')

def esummit(request):
    return render(request,'event/esummit.html')

def vl(request):
    return render(request,'event/vl.html')