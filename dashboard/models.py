from django.db import models

class TuMieszkam(models.Model):
    plik = models.FileField(upload_to='tumieszkam/')
    # uploads / % Y / % m / % d /
    opis = models.CharField(max_length=100)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    okladka = models.ImageField(upload_to='tumieszkam/')


class Przetargi(models.Model):
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    tytul = models.CharField(max_length=255)
    opis = models.TextField(max_length=8000)
    termin_skladania = models.DateTimeField()
    otwarcie_ofert = models.DateTimeField()
    zamkniecie_ofert = models.DateTimeField()


