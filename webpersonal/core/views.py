from django.shortcuts import render, HttpResponse

# HttpResponse permet respondre
# davant una peticio retornant
# un codi (per exemple un codi
# html)

#html_base="""
#    <h1>La meva web personal</h1>
#    <ul>
#        <li><a href="/">Home</a></li>
#        <li><a href="/about-me">Referent a</a></li>
#        <li><a href="/portafoli">Portafoli a</a></li>
#        <li><a href="/contacte">Contacte</a></li>
#    </ul>
#"""

#def home(request):
#    return(HttpResponse(html_base+"""
#    <h2>Portada</h2>
#    <p>Aixo es la portada</p>
#    """))
    # Ara li hem de dir a django
    # a quina url volem posar el
    # codi html creat

# Create your views here.

def home(request):
    return(render(request,'core/home.html'))

def about(request):
    return(render(request,'core/referent.html'))

def portafoli(request):
    return(render(request,'core/portafoli.html'))

def contacte(request):
    return(render(request,'core/contacte.html'))
