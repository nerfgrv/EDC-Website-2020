from django.shortcuts import render
from django.views.generic import DetailView, CreateView , UpdateView ,DeleteView
from django.urls import reverse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields=['title','content','blog_image','author','about_the_author','author_image']

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

class PostUpdateView(UpdateView):
    model = Post
    fields=['title','content','blog_image','author','about_the_author','author_image']

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('blog-home')
