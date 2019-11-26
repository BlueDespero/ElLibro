from django.db import models
from django.urls import reverse
import uuid

class Gatunek(models.Model):
    nazwa = models.CharField(max_length=30, help_text="Wprowadź gatunek literacki.")

    def __str__(self):
        return self.nazwa

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=150, help_text="Wprowadź tytuł książki.")

    def __str__(self):
        return self.tytul

    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    streszczenie = models.TextField(max_length=1000, help_text="Krótkie streszczenie")

    gatunek = models.ManyToManyField(Gatunek, help_text = "Wybierz gatunek")

    def podane_gatunki(self):
        return ', '.join(gatunek.nazwa for gatunek in self.gatunek.all())
    podane_gatunki.short_description = "Gatunki"

    def get_absolute_url(self):
        return reverse('ksiazka-szczegoly', args=[str(self.id)])

    class Meta:
        ordering = ['tytul']

class Autor(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s"%(self.imie, self.nazwisko)

    data_urodzenia = models.DateField(null=True, blank = True)
    data_smierci = models.DateField(null=True, blank = True)

    class Meta:
        ordering = ['imie', 'nazwisko']

    def get_absolute_url(self):
        return reverse('autor-szczegoly', args=[str(self.id)])

class Egzemplarz(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, help_text="Unikatowe ID egzemplarza książki.")
    ksiazka = models.ForeignKey('Ksiazka', on_delete = models.SET_NULL, null=True)
    data_zwrotu = models.DateField(null=True, blank=True)
    #pozyczyl = models.ForeignKey(Uzytkownik, on_delete=models.SET_NULL, null=True, blank=True)

    status_wyporzyczenia = (
        ('W', 'Wypożyczona'),
        ('D', 'Dostepna'),
        ('R', 'Zarezerwowana')
    )

    status = models.CharField(max_length=1, choices=status_wyporzyczenia, blank=True, default='D', help_text='Wprowadź status ksiazki')

    def __str__(self):
        return self.ksiazka.tytul


