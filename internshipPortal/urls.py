from django.urls import path
from . import views
from .views import InternshipDetailView, InternshipCreateView

urlpatterns = [
    path('internships/', views.internships, name='internships'),
    path('create_internship', views.InternshipCreateView,),
    path('internships/<int:pk>', InternshipDetailView.as_view(), name='internship-detail'),
    path('venture_capitalist/', views.VentureCapitalist, name='venture-capitalist'),
    path('create_vencap', views.VenCapCreateView,),
]