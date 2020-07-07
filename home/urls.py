from django.urls import path
from . import views

urlpatterns = [
    path('',			views.home,		name='home'),
    path('our-team/',	views.team,	name='our-team'),
    path('our-team1/',	views.team1,	name='our-team'),
]
