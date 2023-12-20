from django.db import models
from ckeditor.fields import RichTextField


class TuMieszkam(models.Model):
    plik = models.FileField(upload_to='tumieszkam/')
    # uploads / % Y / % m / % d /
    opis = models.CharField(max_length=100)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    okladka = models.ImageField(upload_to='tumieszkam/')


class Przetargi(models.Model):
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    tytul = models.CharField(max_length=255)
    opis = RichTextField(max_length=8000)
    termin_skladania = models.DateTimeField()
    otwarcie_ofert = models.DateTimeField()
    zamkniecie_ofert = models.DateTimeField()

    def __str__(self):
        return self.tytul


class Kalendarium(models.Model):
    data = models.CharField(max_length=100)
    opis = RichTextField(max_length=8000)


class Pliki(models.Model):
    plik = models.FileField(upload_to='pliki/')
    opis = RichTextField(max_length=1000)


class Aktualnosci(models.Model):
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    tytul = models.CharField(max_length=255)
    opis = RichTextField(max_length=8000)
    grafika = models.ImageField(upload_to='aktualnosci/')


# class Kategoria(models.Model):
#     album = models.CharField(max_length=100, null=False, blank=False)
#
#
# class Galeria(models.Model):
#     kategoria_galeria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, related_name="Kategoria", default="1")
#     opis = models.CharField(max_length=100)
#     data_utworzenia = models.DateTimeField(auto_now_add=True)
#     zdjecie = models.ImageField(upload_to='galeria/')
