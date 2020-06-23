from django.urls import path
from .views import NavBar

urlpatterns = [
    path('navbar/', NavBar),
]
