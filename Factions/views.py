from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Government

class Home(ListView):
    queryset = Government.objects.all
    template_name = 'Home/index.html'
class GovernmentList(ListView):
    queryset = Government.objects.all
    context_object_name = 'Government'
    template_name = 'Government/list.html'
    
def Government_detail(request, year, month, day, name):
    gov = get_object_or_404(Government, slug=gov,
                            added__year= year,
                            added__month= month,
                            added__day = day,
                            )
    return render(request, 'Governments/detail.html',
                  {'Government': gov})