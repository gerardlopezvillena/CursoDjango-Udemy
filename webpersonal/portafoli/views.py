from django.shortcuts import render
from .models import Project

# Create your views here.
def portafoli(request):
    projects=Project.objects.all()
    # mesta creant una llista anomenada projects que inclou
    # tots els objectes creats per el model Project (que es
    # una classe)
    return(render(request,'portafoli/portafoli.html', {'projects':projects}))
    # puc afegir totes les varibles que vulgui a la vista definint
    # una clau al diccionari i posant com a valor de la clau, la
    # variable dessitjada. A aquest diccionari sel coneix com a
    # diccionari de context

