from django.apps import AppConfig


class PortafoliConfig(AppConfig):
    name = 'portafoli'
    verbose_name = 'Portafoli' 
    # latribut 'name' no es pot
    # canviar ja que va lligat
    # a la aplicacio, pero si volem
    # canviar el nom que surt al
    # panell dadministracio de
    # django, ho podem fer
    # utilitzant latribut
    # verbose_name. A mes hem
    # de modificar larxiu settings
    # de la carpeta principal
    # (en aquest cas: webpersonal)
    # i el que posarem es:
    # 'portfoli.apps.PortafolioConfig'
    # en definitiva, estic cridant
    # la classe daquest fitxer

