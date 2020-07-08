from django.urls import path
from . import views
from .views import InvestorCreateView, InvestorDeleteView, InvestorUpdateView

urlpatterns = [
    path('investors/', views.investors, name='investors'),
    path('create_investor', views.InvestorCreateView,),
    path('investors/<int:pk>/delete', InvestorDeleteView.as_view(), name='investor-delete'),
    path('investors/<int:pk>/update', InvestorUpdateView.as_view(), name='investor-update'),

	]