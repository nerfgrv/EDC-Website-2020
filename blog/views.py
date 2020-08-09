from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.utils.decorators import method_decorator
from .models import Post
from .forms import PostCreateForm, PostUpdateForm
from user.models import User


def home(request):
    if request.user.is_authenticated and request.user.is_team:
        posts = Post.objects.order_by('-date_published')
    else:
        posts = Post.objects.filter(
            is_published=True).order_by('-date_published')

    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


class PostDetailView(DetailView):
    model = Post


def PostCreateView(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your submission has been sent to our team for review. You will be notified via e-mail if it is published.')

            return HttpResponseRedirect(reverse('blog-home'))

    else:
        form = PostCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/post_form.html', context)


def PostUpdateView(request, pk):
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES,
                              instance=Post.objects.filter(id=pk).first())
        if form.is_valid():
            if request.user.is_team:
                form.save()
                messages.success(request, 'Your blog has been published.')
                return HttpResponseRedirect(reverse('blog-home'))
            else:
                messages.warning(
                    request, 'You do not have the perimission to update this blog.')

    else:
        form = PostUpdateForm(instance=Post.objects.filter(id=pk).first())

    context = {
        'form': form
    }

    return render(request, 'blog/post_form.html', context)


@method_decorator(user_passes_test(lambda u: u.is_authenticated and u.is_team), name='dispatch')
class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('blog-home')


def magazine(request):
    return render(request, 'blog/bizfanatics.html')
