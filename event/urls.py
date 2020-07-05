from django.urls import path
from . import views

urlpatterns = [
    path('',views.events,	name='events'),
    path('e-summit/',views.esummit,name='esummit'),
    path('venture-lab/',views.vl,name='vl'),
    path('startup-weekend/',views.starteco,name='startupweekend'),
    path('e-talks/',views.etalk,name='etalks'),
    path('e-talks2/',views.etalk2,name='etalks2'),
]
