from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from LaBiblioteca.models import Ksiazka, Autor, Egzemplarz, Gatunek

def HomepageView(request):

    num_ksiazki = Ksiazka.objects.all().count()
    num_wszystkie_egzemplarze = Egzemplarz.objects.all().count()
    num_dostepne_egzemplarze = Egzemplarz.objects.filter(status__exact='a').count()
    num_autor = Autor.objects.count()
    
    context = {
        'num_ksiazki': num_ksiazki,
        'num_wszystkie_egzemplarze': num_wszystkie_egzemplarze,
        'num_dostepne_egzemplarze': num_dostepne_egzemplarze,
        'num_autor': num_autor,
    }

    return render(request, 'homepage.html', context=context)