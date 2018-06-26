from django.db import models
# els models, son classes que et generen
# instancies que es guardaran a la bbdd

# Create your models here.
class Project(models.Model):
    # La classe Projedt hereda de la classe models.Model
    # que el que et genera es una taula a la base de dades.
    # Les taules tenen files i columnes, i cada atribut
    # daquesta classes sera uha xooumna diferent
    title= models.CharField(max_length=200, verbose_name="titol")
    # cada atribut es una columna (aixo esta definit aixi a models.Model
    description=models.TextField(verbose_name="descripcio")
    image=models.ImageField(verbose_name="imatge")
    created=models.DateTimeField(auto_now_add=True, verbose_name="creat")
    updated=models.DateTimeField(auto_now=True, verbose_name="modificat")
    class Meta():
        verbose_name="projecte"
        # modifico el nom en angles
        # del model Projects (ja se
        # que ho he creat jo, pero
        # era per mantenir una
        # llogica en el codi, en
        # que tot esta en angles
        verbose_name_plural="projectes"
        # poso el plural
        ordering=["-created"]
        # ordeno els projectes
        # per data de creacio
        # com ho he posat negatiu
        # vol dir que sordena a la
        # inversa, es a dir, del
        # projecte mes nou al mes
        # antic

    def __str__(self):
        return(self.title)
