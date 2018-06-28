from django.shortcuts import render

# Create your views here.
def portafoli(request):
    return(render(request,'portafoli/portafoli.html'))

