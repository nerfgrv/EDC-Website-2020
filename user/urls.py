from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as core_views
from . import views

urlpatterns = [
    
    path('signup',	core_views.signup,name='signup'),
    path('signup/student', 	core_views.register,name='signup-student'),
    path('login/student/', auth_views.LoginView.as_view(template_name='user/login-student.html'),name='login'),
    path('profile/student', core_views.profile,name='profile/student/'),
    path('logout/student/', auth_views.LogoutView.as_view(template_name='user/logout-student.html'), name='logout'),
    path('signup/startup', core_views.registerstup,name='signup-startup'),
    path('login/startup/',auth_views.LoginView.as_view(template_name='user/login-startup.html'),name='login'),
    path('profile/startup', core_views.profilestup,name='profile-startup/'),
    path('logout/startup/', auth_views.LogoutView.as_view(template_name='user/logout-startup.html'), 	name='logout'),
    
]
