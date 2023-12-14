from django.shortcuts import render, redirect, HttpResponse
from dashboard.forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TuMieszkam
from .models import Przetargi
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

def tu_mieszkam(request):
    magazyn = TuMieszkam.objects.all()
    context = {"records": magazyn}

    return render(request, "tu-mieszkam.html", context = context)


def przetargi(request):
    przetarg= Przetargi.objects.all()
    context = {"records_przetargi": przetarg}

    return render(request, "przetargi.html", context = context)

