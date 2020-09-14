from django.urls import path
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .models import Post
from . import views

urlpatterns = [
    path('blogs/<int:pg>/', 		            views.home, 				name='blog-home'),
    path('blogs/<int:pg>/<int:pk>/',            PostDetailView, 	        name='post-detail'),
    path('blogs/write/' , 			            PostCreateView, 			name='post-create'),
    path('blogs/<int:pg>/<int:pk>/update/', 	PostUpdateView, 			name='post-update'),
    path('blogs/<int:pg>/<int:pk>/delete/', 	PostDeleteView.as_view(), 	name='post-delete'),
    path('blogs/bizfanatics/',                  views.magazine,	            name='magazine'),
]