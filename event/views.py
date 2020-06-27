from django.shortcuts import render

# Create your views here.
def events(request):
    return render(request,'event/events.html')