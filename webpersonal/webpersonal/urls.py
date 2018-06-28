"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portafoli import views as portafoli_views

from django.conf import settings
# aixo ens permet accedir al
# fitxer settings, i per tant,
# quan en mode de DEBUG del
# projecte volguem carregar un arxiu
# django ens ho permeti

urlpatterns = [
    path('',core_views.home,name='home'),
    #el path indica a quina extensio
    #de la pagina we posem el view
    #indicat. En el cas que estigui
    #buit es posa a la arrel
    path('about-me',core_views.about,name='about'),
    path('portafoli',portafoli_views.portafoli,name='portafoli'),
    path('contacte',core_views.contacte,name='contacte'),
    path('admin/',admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
