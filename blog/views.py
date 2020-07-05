from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Post


def home(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields=['title','content']

    def form_valid(self, form):
    	form.instance.author=self.request.user
    	return super().form_valid(form)


def home1(request):
    return render(request, 'blog/home1.html')
