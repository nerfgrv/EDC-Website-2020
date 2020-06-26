from django.urls import path
from . import views

urlpatterns = [
    path('navbar/',		views.NavBar),
    path('',			views.home,		name='home'),
    path('our-team/',	views.team,	name='our-team'),
]
