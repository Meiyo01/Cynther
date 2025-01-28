from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Government

class GovernmentListView(ListView):
    queryset = Government.objects.all()
    context_object_name = 'Government'
    paginate_by = 3
    template_name = 'Factions/Governments/list.html'
    
def Government_detail(request, year, month, day, name):
    gov = get_object_or_404(Government,  name = Government.name,
                            added__year= year,
                            added__month= month,
                            added__day = day,
                            )
    return render(request, 'Factions/Governments/detail.html',
                  {'Government': gov})