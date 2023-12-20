from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from dashboard.forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TuMieszkam
from .models import Przetargi
from .models import Kalendarium
from .models import Pliki
from .models import Aktualnosci
# from .models import Galeria
from django.http import FileResponse
import os
# homepage view
def home(request):
    return render(request, ("dashboard.html"))


# register view
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "register.html", context=context)


# login view
def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Zalogowano")

                return redirect("dashboard")

    context = {"form": form}
    return render(request, "login.html", context=context)


# logout view
def logout_view(request):
    auth.logout(request)
    messages.success(request, "Wylogowano")
    return redirect("login")


@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")


def dashboard_main(request):
    return render(request, "dashboard.html")


def iso_iso(request):
    return render(request, "iso-iso.html")

def iso_polityka(request):
    return render(request, "iso-polityka.html")

def iso_badanie(request):
    return render(request, "iso-badanie.html")

def wspolnoty(request):
    return render(request, "wspolnoty.html")


def kontakt(request):
    return render(request, "kontakt.html")


def spoldzielnia_organy(request):
    return render(request, "spoldzielnia-organy.html")

def spoldzielnia_radanadzorcza(request):
    return render(request, "spoldzielnia-radanadzorcza.html")

def spoldzielnia_radyosiedli(request):
    return render(request, "spoldzielnia-radyosiedli.html")

def spoldzielnia_zarzad(request):
    return render(request, "spoldzielnia-zarzad.html")

def spoldzielnia_administracje(request):
    return render(request, "spoldzielnia-administracje.html")

def spoldzielnia_akty(request):
    return render(request, "spoldzielnia-akty.html")

def spoldzielnia_rodo(request):
    return render(request, "spoldzielnia-rodo.html")


def spoldzielnia_statut(request):
    return render(request, "spoldzielnia-statut.html")


def spoldzielnia_ue(request):
    return render(request, "spoldzielnia-ue.html")


def spoldzielnia_samorzad(request):
    return render(request, "spoldzielnia-samorzad.html")


def spoldzielnia_kalendarium(request):
    kalendarz = Kalendarium.objects.all()
    context = {"records_kalendarium": kalendarz}
    return render(request, "spoldzielnia-kalendarium.html", context=context)

def tu_mieszkam(request):
    magazyn = TuMieszkam.objects.all()
    context = {"records": magazyn}

    return render(request, "tu-mieszkam.html", context = context)


def pliki(request):
    magazyn_pliki= Pliki.objects.all()
    context = {"records_pliki": magazyn_pliki}

    return render(request, "pobierz.html", context = context)


def przetargi(request):
    przetargi_all= Przetargi.objects.all()
    context = {"records_przetargi": przetargi_all}

    return render(request, "przetargi.html", context = context)

def przetargi_details(request, pk):
    przetarg= Przetargi.objects.get(id=pk)
    context = {"records_przetargi_id": przetarg}

    return render(request, "przetargi-details.html", context = context)


def aktualnosci(request):
    aktualnosci_all= Aktualnosci.objects.all()
    context = {"records_aktualnosci": aktualnosci_all}

    return render(request, "aktualnosci.html", context = context)

def aktualnosci_details(request, pk):
    aktualnosc= Aktualnosci.objects.get(id=pk)
    context = {"records_aktualnosc_id": aktualnosc}

    return render(request, "aktualnosci-details.html", context = context)


# def galeria(request):
#     galeria_all= Galeria.objects.all()
#     context = {"records_galeria": galeria_all}
#
#     return render(request, "galeria.html", context = context)
#
# def galeria_details(request, pk):
#     album= Galeria.objects.get(id=pk)
#     context = {"records_galeria_id": album}
#
#     return render(request, "galeria-details.html", context = context)
