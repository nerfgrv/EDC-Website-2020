from django.urls import path
from . import views

urlpatterns = [
    path('',views.tnc,name='tnc_home'),
	]