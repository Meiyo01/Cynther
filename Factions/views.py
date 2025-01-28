from django.shortcuts import render, get_object_or_404
from .models import Government

def Government_list(request):
    gov = Government.objects.all()
    return render (request,
                   'Factions/Governments/list.html',
                   {'Government': gov})