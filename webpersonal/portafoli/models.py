from django.db import models
# els models, son classes que et generen
# instancies que es guardaran a la bbdd

# Create your models here.
class Project(models.model):
    # La classe Projedt hereda de la classe models.model
    # que el que et genera es una taula a la base de dades.
    # Les taules tenen files i columnes, i cada atribut
    # daquesta classes sera uha xooumna diferent
    title= # cada atribut es una columna (aixo esta definit
        # aixi a models.model
    description=
