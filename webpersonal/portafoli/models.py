from django.db import models
# els models, son classes que et generen
# instancies que es guardaran a la bbdd

# Create your models here.
class Project(models.Model):
    # La classe Projedt hereda de la classe models.Model
    # que el que et genera es una taula a la base de dades.
    # Les taules tenen files i columnes, i cada atribut
    # daquesta classes sera uha xooumna diferent
    title= models.CharField(max_length=200)
    # cada atribut es una columna (aixo esta definit aixi a models.Model
    description=models.TextField()
    image=models.ImageField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
