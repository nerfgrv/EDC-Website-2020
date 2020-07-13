from django.urls import path
from . import views
from .views import InvestorCreateView, InvestorDeleteView, InvestorUpdateView

urlpatterns = [
    path('investors/', views.Investors, name='investors'),
    path('investors/create/', views.InvestorCreateView, name='create-investor'),
    path('investors/<int:pk>/delete/', InvestorDeleteView.as_view(), name='investor-delete'),
    path('investors/<int:pk>/update/', InvestorUpdateView, name='investor-update'),

	]