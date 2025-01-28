from django.shortcuts import render
from django.views.generic import ListView
from .models import Government

class GovernmentListView(ListView):
    queryset = Government.objects.all()
    context_object_name = 'Faction'
    paginate_by = 3
    template_name = 'Factions/Governments/list.html'