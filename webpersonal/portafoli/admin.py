from django.contrib import admin
from .models import  Project

# Register your models here.

# Configurem el panell de controo per a que
# es vegin la data de creacio i la data de
# modificacio del projecte
class ProjectAdmin(admin.ModelAdmin):
    # Puc posar el nom que vulgui pero sembla ser
    # que hi ha consens en aquest tipus de nom
    readonly_fields=('created', 'updated')

admin.site.register(Project, ProjectAdmin)
# he registrat els dos models Project i ProjectAdmin
