from django.urls import path
from . import views

app_name = 'Factions'

urlpatterns = [
    path('', views.GovernmentListView.as_view(), name='government.list'),
    path('<int:year>/<int:month>/<int:day>/<str:name>', views.Government_detail, name='Government_detail'),
]
