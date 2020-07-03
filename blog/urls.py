from django.urls import path
from .views import PostDetailView
from .models import Post
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
]