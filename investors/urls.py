from django.urls import path
from . import views

urlpatterns = [
    path('',views.investors,name='investor_home'),
	]