from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('signup/student/', core_views.studentregister,												name='student-signup'),
    path('signup/startup/', core_views.startupregister, 											name='startup-signup'),
    path('login/student/', 	auth_views.LoginView.as_view(template_name='user/login-student.html'),	name='student-login'),
    path('login/startup/',	auth_views.LoginView.as_view(template_name='user/login-startup.html'),	name='startup-login'),
    path('logout/student/', auth_views.LogoutView.as_view(template_name='user/logout-student.html'),name='logout'),
    path('logout/startup/', auth_views.LogoutView.as_view(template_name='user/logout-startup.html'),name='logout'),
    path('profile/update/', core_views.profileupdate,												name='student-profile-update'),
    path('profile/student/',core_views.studentprofile,												name='profile/student/'),
    path('profile/startup/',core_views.startupprofile,												name='profile-startup/'),
    
]
if settings.DEBUG: 
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )
