from django.urls import path
from . import views

urlpatterns = [
    path('',views.events,	name='events'),
    path('e-summit',views.esummit,name='esummit'),
    path('venture-lab',views.vl,name='vl'),
]
