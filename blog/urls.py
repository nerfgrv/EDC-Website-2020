from django.urls import path
from .views import PostDetailView,PostCreateView
from .models import Post
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='var-detail'),
    path('post/new/' , PostCreateView.as_view(), name='post-create'),
]