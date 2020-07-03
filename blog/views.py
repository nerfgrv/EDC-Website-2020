from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostDetailView(DetailView):
    model = Post
