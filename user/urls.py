from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as core_views
from . import views

urlpatterns = [
    path('signup/', 	core_views.register, 												name='signup'),
    path('login/', 		auth_views.LoginView.as_view(template_name='user/login.html'), 		name='login'),
    path('profile/', 	core_views.profile, 												name='profile'),
    path('logout/', 	auth_views.LogoutView.as_view(template_name='user/logout.html'), 	name='logout'),
]
