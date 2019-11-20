from django.contrib import admin
from LaBiblioteca.models import Ksiazka,Egzemplarz,Autor,Gatunek

class AutorAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'data_smierci')

admin.site.register(Autor, AutorAdmin)

class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'podane_gatunki')
    
admin.site.register(Ksiazka, KsiazkaAdmin)
admin.site.register(Egzemplarz)
admin.site.register(Gatunek)