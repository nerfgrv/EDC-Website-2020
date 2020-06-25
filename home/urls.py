from django.urls import path
from . import views

urlpatterns = [
    path('navbar/',views.NavBar),
    path('',views.home,name='home-page'),
    path('aboutus/',views.aboutus,name='aboutus-page'),
]
