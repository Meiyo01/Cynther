from django.urls import path
from . import views

app_name = 'Factions'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('Government/', views.GovernmentList.as_view(), name='government_list'),
    path('Government/List/', views.Government_detail, name='Government_detail'),
]
