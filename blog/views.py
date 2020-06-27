from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post


def home(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostDetailView(DetailView):
    model = Post


def home1(request):
    return render(request, 'blog/home1.html')
