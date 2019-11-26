from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

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

class BookListView(generic.ListView):
    model = Ksiazka
    paginate_by = 10
    context_object_name = 'lista_ksiazek'
    queryset = Ksiazka.objects.all()
    template_name = 'book_list.html'

class AutorListView(generic.ListView):
    model = Autor
    paginate_by = 10
    context_object_name = 'lista_autorow'
    queryset = Autor.objects.all()
    template_name = 'author_list.html'

class BookDetailView(generic.DeleteView):
    model = Ksiazka
    template_name = 'book_detail.html'

class AutorDetailView(generic.DeleteView):
    model = Autor
    template_name = 'author_detail.html'