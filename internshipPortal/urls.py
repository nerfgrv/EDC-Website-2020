from django.urls import path
from . import views
from .views import (InternshipDetailView, InternshipUpdateView, InternshipDeleteView, VenCapDeleteView, VenCapUpdateView)

urlpatterns = [
    path('internships/', views.internships, name='internships'),
    path('create_internship', views.InternshipCreateView,),
    path('internships/<int:pk>', InternshipDetailView.as_view(), name='internship-detail'),
    path('internships/<int:pk>/update', InternshipUpdateView.as_view(), name='internship-update'),
    path('internships/<int:pk>/delete', InternshipDeleteView.as_view(), name='internship-delete'),
    ################################################################################################
    path('venture_capitalist/', views.VentureCapitalist, name='venture-capitalist'), 
    path('create_vencap', views.VenCapCreateView,),
    path('venture_capitalist/<int:pk>/update', VenCapUpdateView.as_view(), name='vencap-update'),
    path('venture_capitalist/<int:pk>/delete', VenCapDeleteView.as_view(), name='vencap-delete'),
    
]