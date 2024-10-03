from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_expense, name='add_expense'),
    path('summary/date/', views.summary_by_date, name='summary_by_date'),
    path('summary/category/', views.summary_by_category, name='summary_by_category'),
]